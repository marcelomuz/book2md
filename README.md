# Book2MD

Conversor automático de arquivos PDF e ePUB para formato Markdown estruturado.

## Visão Geral

Book2MD é uma ferramenta Python para converter facilmente arquivos PDF e ePUB para Markdown estruturado. O script utiliza o Docling como conversor principal, com fallback para o Calibre em arquivos ePUB que o Docling não consegue processar adequadamente.

## Funcionalidades

- Conversão de PDFs para Markdown estruturado usando Docling
- Conversão de ePUBs para Markdown usando Docling ou Calibre (fallback automático)
- Modo de escaneamento único (processamento em lote)
- Modo de observação contínua (processamento de novos arquivos)
- Logs detalhados de cada execução
- Suporte a configuração via variáveis de ambiente (.env)

## Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)
- Calibre (para conversão de fallback de ePUBs)

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/marcelomuz/book2md.git
   cd book2md
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure o ambiente:
   ```bash
   cp .env.example .env
   # Edite o arquivo .env com seus caminhos
   ```

## Uso

### Conversão em Lote

Para processar todos os arquivos PDF e ePUB no diretório de entrada:

```bash
python -m scripts.convert
```

### Modo de Observação

Para iniciar o modo de observação que processa novos arquivos automaticamente:

```bash
python -m scripts.convert --watch
```

## Configuração

As configurações podem ser definidas através de variáveis de ambiente ou do arquivo `config/config.yml`. As variáveis de ambiente têm precedência sobre as configurações no arquivo YAML.

### Variáveis de Ambiente

- `BOOK2MD_INPUT_DIR`: Diretório onde estão os arquivos a serem convertidos
- `BOOK2MD_OUTPUT_MD`: Diretório onde serão salvos os arquivos Markdown
- `BOOK2MD_OUTPUT_LOGS`: Diretório onde serão salvos os logs
- `BOOK2MD_RETRY_ATTEMPTS`: Número de tentativas para converter um arquivo
- `BOOK2MD_WATCH_MODE`: Modo de observação habilitado por padrão (true/false)

## Estrutura do Projeto

```
book2md/
├── config/
│   └── config.yml     # Configurações principais
├── input/             # Diretório de entrada para PDFs/ePUBs
├── output/
│   ├── md/            # Arquivos Markdown convertidos
│   └── logs/          # Logs de execução
└── scripts/
    ├── convert.py     # Script principal de conversão
    └── utils.py       # Funções auxiliares
```

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para detalhes.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.
