# Pipeline de Conversão do Book2MD

Este documento explica em detalhes como funciona o processo de conversão de arquivos PDF e ePUB para Markdown estruturado no Book2MD.

## Visão Geral do Pipeline

O processo de conversão ocorre através das seguintes etapas:

1. **Detecção de Arquivos**: O sistema identifica arquivos PDF e ePUB no diretório de entrada.
2. **Conversão Principal**: Tentativa de conversão utilizando a biblioteca Docling.
3. **Fallback para ePUB**: Se a conversão de um arquivo ePUB falhar, o sistema utiliza o Calibre como alternativa.
4. **Pós-processamento**: Conversão adicional de HTML para Markdown quando necessário.
5. **Registro de Logs**: Documentação detalhada de cada etapa do processo.

## Processo Detalhado

### 1. Detecção de Arquivos

O sistema escaneia o diretório de entrada (e seus subdiretórios) em busca de arquivos com extensão `.pdf` ou `.epub`. Isso é feito através do método `Path.rglob()` que realiza uma busca recursiva.

```python
for path in input_dir.rglob("*"):
    if path.suffix.lower() in SUPPORTED_EXT and path.is_file():
        # Processa o arquivo
```

### 2. Conversão Principal com Docling

Para cada arquivo encontrado, o sistema tenta convertê-lo usando a biblioteca Docling:

```python
converter = DocumentConverter()
result = converter.convert(str(file_path))
md = result.document.export_to_markdown()
```

O Docling é uma biblioteca de processamento de documentos que:
- Extrai texto de PDFs
- Identifica a estrutura do documento (títulos, subtítulos, parágrafos)
- Preserva formatação básica (negrito, itálico, listas)
- Gera um documento Markdown estruturado

### 3. Fallback para ePUB com Calibre

Se a conversão de um arquivo ePUB falhar usando o Docling, o sistema automaticamente tenta uma segunda abordagem utilizando o Calibre:

```python
if path.suffix.lower() == ".epub" and status == "FALHOU":
    cmd = [CALIBRE_CMD, str(path), str(epub_md), "--markdown"]
    subprocess.run(cmd, check=True)
```

O Calibre é chamado via linha de comando usando o utilitário `ebook-convert`, que:
- É mais robusto para a conversão de ePUBs complexos
- Pode gerar Markdown diretamente ou HTML intermediário
- Preserva mais elementos de formatação do ePUB original

### 4. Pós-processamento com Markdownify

Se a saída do Calibre for HTML em vez de Markdown (o que acontece em alguns casos), o sistema utiliza a biblioteca Markdownify para converter o HTML para Markdown:

```python
if epub_md.suffix.lower() == ".html":
    html = epub_md.read_text(encoding="utf-8")
    md = mdify(html)
    epub_md.write_text(md, encoding="utf-8")
```

### 5. Registro de Logs

Cada operação é registrada em um arquivo de log em formato Markdown, contendo:
- Data e hora da execução
- Arquivos processados
- Status da conversão (sucesso ou falha)
- Número estimado de páginas
- Tempo de processamento
- Observações ou mensagens de erro

## Fluxograma do Pipeline

```
┌─────────────────┐
│ Entrada: PDF ou │
│      ePUB       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Tentativa com  │
│     Docling     │
└────────┬────────┘
         │
         ▼
     ┌───────┐      ┌─────────────────┐
     │ Falha?│─Sim──►  É um ePUB?     │
     └───┬───┘      └────────┬────────┘
         │                   │
         Não                 Sim
         │                   │
         │                   ▼
         │          ┌─────────────────┐
         │          │  Tentativa com  │
         │          │     Calibre     │
         │          └────────┬────────┘
         │                   │
         │                   ▼
         │          ┌─────────────────┐
         │          │ Saída é HTML?   │
         │          └────────┬────────┘
         │                   │
         │                   Sim
         │                   │
         │                   ▼
         │          ┌─────────────────┐
         │          │ Conversão HTML  │
         │          │  para Markdown  │
         │          └────────┬────────┘
         │                   │
         ▼                   ▼
┌─────────────────────────────────────┐
│         Saída: Markdown             │
└─────────────────────────────────────┘
```

## Mecanismos de Tolerância a Falhas

O sistema inclui vários mecanismos para aumentar a taxa de sucesso das conversões:

1. **Múltiplas Tentativas**: O número de tentativas com o Docling é configurável via `retry_attempts`.
2. **Pipeline de Fallback**: Se o Docling falhar para ePUBs, o Calibre é usado automaticamente.
3. **Conversão de Formato Intermediário**: Suporte a conversão HTML -> Markdown quando necessário.
4. **Logs Detalhados**: Informações precisas sobre falhas para depuração.

## Limitações Conhecidas

- **PDFs com OCR de Baixa Qualidade**: Podem resultar em texto mal formatado.
- **PDFs com Proteção DRM**: Não podem ser processados sem remoção prévia da proteção.
- **ePUBs Complexos**: Elementos avançados como equações matemáticas ou diagramas complexos podem não ser convertidos corretamente.
- **Tabelas**: Conversão de tabelas complexas pode resultar em formatação inadequada.