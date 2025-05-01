#!/usr/bin/env python3
"""Convert PDF/ePUB files in input_dir to Markdown using Docling.

Usage:
    python -m scripts.convert [--watch]
"""
import argparse
import datetime as dt
import os
import pathlib
import shutil
import subprocess
import sys
import traceback

import yaml
from docling.document_converter import DocumentConverter
from dotenv import load_dotenv
from loguru import logger
from markdownify import markdownify as mdify
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

# Carrega variáveis do arquivo .env
load_dotenv()

sys.path.append(str(pathlib.Path(__file__).resolve().parent))
from utils import ensure_parent, setup_logger, timed  # noqa: E402


SUPPORTED_EXT = {".pdf", ".epub"}


CALIBRE_CMD = "ebook-convert"


def load_cfg():
    cfg_path = pathlib.Path(__file__).parent.parent / "config" / "config.yml"
    cfg = yaml.safe_load(cfg_path.read_text())
    
    # Sobrescreve com variáveis de ambiente se definidas
    if os.getenv("BOOK2MD_INPUT_DIR"):
        cfg["input_dir"] = os.getenv("BOOK2MD_INPUT_DIR")
    if os.getenv("BOOK2MD_OUTPUT_MD"):
        cfg["output_md"] = os.getenv("BOOK2MD_OUTPUT_MD")
    if os.getenv("BOOK2MD_OUTPUT_LOGS"):
        cfg["output_logs"] = os.getenv("BOOK2MD_OUTPUT_LOGS")
    if os.getenv("BOOK2MD_RETRY_ATTEMPTS"):
        cfg["retry_attempts"] = int(os.getenv("BOOK2MD_RETRY_ATTEMPTS"))
    if os.getenv("BOOK2MD_WATCH_MODE"):
        cfg["watch_mode"] = os.getenv("BOOK2MD_WATCH_MODE").lower() == "true"
    
    return cfg


def markdown_log_header(now):
    return f"# Execução {now:%Y-%m-%d %H:%M}\n\n| Arquivo | Tipo | Status | Páginas | Tempo (s) | Obs |\n|---|---|---|---|---|---|"


@timed
def convert_one(file_path: pathlib.Path, out_md_dir: pathlib.Path):
    """Convert a single file and return markdown, pages processed."""
    converter = DocumentConverter()
    result = converter.convert(str(file_path))
    md = result.document.export_to_markdown()
    # naive page count estimate
    pages = md.count("\n# ")
    out_path = out_md_dir / file_path.with_suffix(".md").name
    ensure_parent(out_path)
    out_path.write_text(md, encoding="utf-8")
    return pages


def process_file(path: pathlib.Path, cfg):
    """Process individual file with retries."""
    out_md_dir = pathlib.Path(cfg["output_md"])
    status = "FALHOU"
    pages = "-"
    elapsed = 0.0
    obs = "-"
    max_attempts = cfg.get("retry_attempts", 1)
    for attempt in range(1, max_attempts + 1):
        try:
            pages, elapsed = convert_one(path, out_md_dir)
            status = "OK"
            obs = "-"
            break
        except Exception as e:
            status = "FALHOU"
            obs = str(e)
            if attempt < max_attempts:
                continue
    # ePUB fallback: if file is .epub and failed
    if path.suffix.lower() == ".epub" and status == "FALHOU":
        out_md_dir = pathlib.Path(cfg["output_md"])
        epub_md = out_md_dir / path.with_suffix(".md").name
        # fallback via Calibre
        cmd = [CALIBRE_CMD, str(path), str(epub_md), "--markdown"]
        try:
            subprocess.run(cmd, check=True)
            # if output is HTML, convert via markdownify
            if epub_md.suffix.lower() == ".html":
                html = epub_md.read_text(encoding="utf-8")
                md = mdify(html)
                epub_md.write_text(md, encoding="utf-8")
            status = "OK"
            obs = "fallback: calibre"
        except Exception as e:
            obs = f"calibre_fail: {e}"
            status = "FALHOU"
    return status, pages, elapsed, obs


def scan_and_process(cfg):
    input_dir = pathlib.Path(cfg["input_dir"])
    now = dt.datetime.now()
    log_path = pathlib.Path(cfg["output_logs"]) / f"{now:%Y-%m-%d_%H-%M}.md"
    logger = setup_logger(log_path)
    logger.info(markdown_log_header(now))

    for path in input_dir.rglob("*"):
        if path.suffix.lower() in SUPPORTED_EXT and path.is_file():
            status, pages, elapsed, obs = process_file(path, cfg)
            logger.info(
                f"{path} | {path.suffix.upper()} | {status} | {pages} | {elapsed:.1f} | {obs}"
            )

    logger.info("\n**Fim da execução**")


class WatchHandler(FileSystemEventHandler):
    def __init__(self, cfg):
        self.cfg = cfg

    def on_created(self, event):
        if event.is_directory:
            return
        path = pathlib.Path(event.src_path)
        if path.suffix.lower() in SUPPORTED_EXT:
            process_file(path, self.cfg)


def watch_mode(cfg):
    observer = Observer()
    handler = WatchHandler(cfg)
    observer.schedule(handler, cfg["input_dir"], recursive=True)
    observer.start()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


def main():
    parser = argparse.ArgumentParser(description="Convert PDF/ePUB to Markdown.")
    parser.add_argument("--watch", action="store_true", help="Watch input dir for new files")
    args = parser.parse_args()

    cfg = load_cfg()
    if args.watch or cfg.get("watch_mode"):
        watch_mode(cfg)
    else:
        scan_and_process(cfg)


if __name__ == "__main__":
    main()