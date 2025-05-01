import pathlib, time, functools
from loguru import logger

def timed(func):
    """Decorator to measure execution time of functions."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        return result, elapsed

    return wrapper


def ensure_parent(path: pathlib.Path):
    """Create parent directories if they don't exist."""
    path.parent.mkdir(parents=True, exist_ok=True)


def setup_logger(log_path: pathlib.Path):
    ensure_parent(log_path)
    logger.remove()
    logger.add(log_path, format="{time} | {level} | {message}")
    return logger