# Fluxo de Trabalho Completo do Book2MD

Este guia descreve o fluxo de trabalho completo para utilizar o Book2MD, desde a preparação do ambiente até o processamento final dos documentos.

## 1. Preparação do Ambiente

### 1.1 Requisitos do Sistema

Antes de começar, verifique se seu sistema atende aos seguintes requisitos:

- **Python**: Versão 3.7 ou superior
- **Calibre**: Instalado e disponível no PATH do sistema
- **Espaço em Disco**: Suficiente para armazenar os arquivos de entrada e saída
- **Permissões**: Acesso de leitura/escrita aos diretórios configurados

### 1.2 Instalação do Ambiente

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/book2md.git
   cd book2md
   ```

2. **Crie um ambiente virtual** (recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o arquivo `.env`**:
   ```bash
   cp .env.example .env
   # Edite o arquivo .env com seus caminhos específicos
   ```

### 1.3 Verificação da Instalação

Confirme que tudo está funcionando corretamente:

1. **Verifique o Python**:
   ```bash
   python --version  # Deve mostrar 3.7 ou superior
   ```

2. **Verifique o Calibre**:
   ```bash
   which ebook-convert  # Linux/macOS
   where ebook-convert  # Windows
   ```

3. **Teste a instalação**:
   ```bash
   python -m scripts.convert --help
   ```

## 2. Preparação dos Documentos

### 2.1 Organização dos Arquivos

Organize seus arquivos de forma estruturada para facilitar o processamento:

1. **Estrutura Recomendada**:
   ```
   input/
   ├── livros/
   │   ├── ficção/
   │   └── não-ficção/
   ├── artigos/
   └── documentos/
   ```

2. **Verificação de Arquivos**:
   - Certifique-se de que os PDFs não estão protegidos por senha
   - Para resultados ideais, use PDFs com texto selecionável (não escaneados)
   - Remova DRM de ePUBs, se necessário

### 2.2 Melhores Formatos para Conversão

Para obter melhores resultados:

1. **Formato PDF**:
   - PDFs com texto pesquisável (não apenas imagens)
   - PDFs com estrutura clara de capítulos/seções
   - PDFs sem proteção DRM

2. **Formato ePUB**:
   - ePUBs bem formatados com estrutura de capítulos
   - ePUBs sem proteção DRM
   - Preferencialmente ePUB 3.0 ou superior

## 3. Execução do Processo

### 3.1 Conversão em Lote

Para processar todos os arquivos de uma vez:

```bash
python -m scripts.convert
```

Isso irá:
1. Escanear o diretório de entrada e seus subdiretórios
2. Converter todos os PDFs e ePUBs encontrados
3. Salvar os arquivos Markdown no diretório de saída
4. Gerar um log detalhado do processo

### 3.2 Modo de Observação

Para processar arquivos automaticamente quando adicionados ao diretório:

```bash
python -m scripts.convert --watch
```

Esse modo:
1. Inicia um observador no diretório de entrada
2. Monitora novos arquivos adicionados
3. Converte automaticamente PDFs e ePUBs quando detectados
4. Continua rodando até ser interrompido (Ctrl+C)

### 3.3 Uso com IDEs Agênticas

O Book2MD pode ser facilmente integrado a IDEs agênticas:

1. **Windsurf**:
   - Abra o projeto no Windsurf
   - Configure o comando de execução: `python -m scripts.convert`
   - Utilize a funcionalidade de terminal integrado

2. **Cursor**:
   - Importe o projeto no Cursor
   - Configure o ambiente Python com as dependências
   - Execute diretamente do painel de comandos

3. **Zed**:
   - Abra a pasta do projeto no Zed
   - Configure a tarefa de build para executar o script
   - Use o terminal integrado para iniciar conversões

4. **Trae**:
   - Importe o projeto no Trae
   - Configure o executor para Python 3
   - Utilize os atalhos de execução para iniciar o processo

## 4. Processamento Pós-Conversão

### 4.1 Verificação dos Resultados

Após a conversão, é importante verificar a qualidade dos arquivos gerados:

1. **Verifique a Estrutura do Markdown**:
   - Confirme que os cabeçalhos estão corretos (# para títulos, ## para subtítulos, etc.)
   - Verifique se parágrafos, listas e formatação básica foram preservados

2. **Análise de Problemas Comuns**:
   - Texto sem formatação adequada
   - Quebras de página incorretas
   - Imagens ou tabelas não convertidas

### 4.2 Pós-processamento Manual (se necessário)

Em alguns casos, pode ser necessário um pós-processamento manual:

1. **Correções Comuns**:
   - Ajustar níveis de cabeçalho inconsistentes
   - Corrigir formatação de listas
   - Remover artefatos de conversão

2. **Ferramentas Recomendadas**:
   - VSCode com extensão Markdown All in One
   - Typora ou outro editor Markdown visual
   - Scripts personalizados para correções em lote

### 4.3 Integração com Outros Sistemas

Os arquivos Markdown gerados podem ser facilmente integrados a:

1. **Sistemas de Notas**:
   - Obsidian
   - Notion
   - Joplin

2. **Wikis e Documentação**:
   - GitHub/GitLab Wikis
   - MkDocs
   - Jekyll

3. **Processadores de Texto**:
   - Pandoc para conversão para outros formatos (DOCX, HTML, etc.)
   - Sistemas de publicação baseados em Markdown

## 5. Manutenção do Sistema

### 5.1 Limpeza Regular

Para manter o sistema funcionando adequadamente:

1. **Arquivos Processados**:
   - Mova os arquivos já processados para um diretório de arquivamento
   - Ou remova-os do diretório de entrada quando não forem mais necessários

2. **Logs**:
   - Revise periodicamente os logs em `output/logs/`
   - Arquive logs antigos para manter o diretório organizado

### 5.2 Atualização do Sistema

Mantenha o sistema atualizado:

1. **Atualizações do Repositório**:
   ```bash
   git pull
   pip install -r requirements.txt --upgrade
   ```

2. **Dependências Externas**:
   - Mantenha o Calibre atualizado com a versão mais recente
   - Atualize o Python quando necessário

## 6. Solução de Problemas

### 6.1 Problemas Comuns e Soluções

| Problema | Possível Causa | Solução |
|----------|----------------|----------|
| Falha na conversão de PDF | PDF protegido ou com OCR de baixa qualidade | Verifique se o PDF está protegido e use uma ferramenta de OCR para melhorá-lo |
| Falha na conversão de ePUB | Formato ePUB complexo ou com DRM | Remova o DRM e tente novamente ou verifique se o Calibre está instalado corretamente |
| Erro "calibre_fail" | Calibre não está no PATH ou não está instalado | Instale o Calibre e verifique se `ebook-convert` está disponível no terminal |
| Markdown sem formatação | Falha na detecção de estrutura do documento | Tente ajustar o documento original para ter uma estrutura mais clara |
| Erro de permissão | Permissões insuficientes nos diretórios | Verifique as permissões dos diretórios de entrada e saída |

### 6.2 Comandos de Diagnóstico

Use estes comandos para diagnosticar problemas:

1. **Verificar Ambiente**:
   ```bash
   python -c "import docling, yaml, markdownify; print('OK')"
   ```

2. **Testar Calibre**:
   ```bash
   ebook-convert --version
   ```

3. **Verificar Configuração**:
   ```bash
   python -c "import yaml; print(yaml.safe_load(open('config/config.yml')))"
   ```

4. **Verificar Variáveis de Ambiente**:
   ```bash
   python -c "import os, dotenv; dotenv.load_dotenv(); print(os.environ.get('BOOK2MD_INPUT_DIR'))"
   ```