# Integração com IDEs Agênticas

O Book2MD pode ser facilmente utilizado com IDEs agênticas, permitindo uma experiência mais suave e intuitiva, especialmente para usuários menos familiarizados com linha de comando. Este guia explica como configurar e utilizar o Book2MD com diferentes IDEs agênticas modernas.

## Por que Usar IDEs Agênticas com Book2MD?

IDEs agênticas são ambientes de desenvolvimento que incorporam assistentes de IA para ajudar no desenvolvimento e uso de software. Algumas vantagens de usar o Book2MD com estas IDEs incluem:

- **Interface gráfica amigável**: Menos necessidade de usar o terminal
- **Assistência contextual**: A IA pode ajudar a entender e usar o Book2MD
- **Automação de tarefas**: Simplificação de fluxos de trabalho complexos
- **Depuração e solução de problemas assistidos**: Ajuda para resolver erros
- **Personalização avançada**: Configurações e extensões para necessidades específicas

## Configuração para IDEs Populares

### Windsurf

[Windsurf](https://www.windsurf.dev/) é uma IDE agêntica com forte integração com modelos de linguagem.

#### Configuração Inicial:

1. **Importe o Projeto**:
   - Abra o Windsurf
   - Selecione "Open Folder" e navegue até o diretório do Book2MD

2. **Configure o Ambiente Python**:
   ```python
   # No terminal integrado do Windsurf
   python -m venv venv
   source venv/bin/activate  # ou venv\Scripts\activate no Windows
   pip install -r requirements.txt
   ```

3. **Crie um Arquivo de Tarefa**:
   - Crie um novo arquivo `.windsurf/tasks.json` com o seguinte conteúdo:
   ```json
   {
     "tasks": {
       "convert": {
         "command": "python -m scripts.convert",
         "description": "Converter arquivos PDF/ePUB para Markdown"
       },
       "watch": {
         "command": "python -m scripts.convert --watch",
         "description": "Monitorar diretório de entrada"
       }
     }
   }
   ```

4. **Habilite MCPs (Capacidades Baseadas em Modelo)**:
   - Instale a extensão "Python Development" do Windsurf
   - Habilite "Document Understanding" para melhor análise do código
   - Habilite "File System Operations" para facilitar a manipulação de arquivos

#### Uso:

1. Use o comando `Convert Files` da paleta de comandos (Ctrl+Shift+P)
2. Solicite à IA para "executar o script de conversão nos arquivos do diretório X"
3. Utilize o painel de execução para monitorar o progresso
4. Peça à IA para ajudar a interpretar os logs ou resolver problemas

### Cursor

[Cursor](https://cursor.sh/) é uma IDE baseada em IA focada em programação assistida.

#### Configuração Inicial:

1. **Abra o Projeto**:
   - Inicie o Cursor e selecione "Open Folder"
   - Navegue até o diretório do Book2MD

2. **Configure o Terminal Integrado**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # ou venv\Scripts\activate no Windows
   pip install -r requirements.txt
   ```

3. **Crie Snippets Personalizados**:
   - Acesse "Settings > User Snippets"
   - Adicione snippets para comandos comuns:
   ```json
   {
     "Convert Files": {
       "prefix": "convert",
       "body": ["python -m scripts.convert"],
       "description": "Converter arquivos PDF/ePUB para Markdown"
     },
     "Watch Directory": {
       "prefix": "watch",
       "body": ["python -m scripts.convert --watch"],
       "description": "Monitorar diretório de entrada"
     }
   }
   ```

4. **Configure Capacidades de IA**:
   - Habilite "Enhanced Code Understanding"
   - Ative "File System Intelligence" para manipulação de arquivos

#### Uso:

1. Use o comando `Ctrl+I` para abrir o assistente de IA
2. Digite: "Converter os PDFs do diretório input para Markdown"
3. O assistente pode gerar o comando necessário e explicar opções
4. Use F5 para executar o script diretamente do editor

### Zed

[Zed](https://zed.dev/) é uma IDE colaborativa com recursos de IA integrados.

#### Configuração Inicial:

1. **Clone o Repositório**:
   - Abra Zed
   - Use "File > Open..." para abrir o diretório do Book2MD

2. **Configure o Ambiente**:
   - No painel de terminal, execute:
   ```bash
   python -m venv venv
   source venv/bin/activate  # ou venv\Scripts\activate no Windows
   pip install -r requirements.txt
   ```

3. **Crie um Arquivo de Tarefas**:
   - Crie `.zed/tasks.json` com:
   ```json
   {
     "tasks": {
       "book2md-convert": {
         "command": "python -m scripts.convert",
         "working_directory": "${workspace_dir}",
         "environment": {
           "PYTHONPATH": "${workspace_dir}"
         }
       },
       "book2md-watch": {
         "command": "python -m scripts.convert --watch",
         "working_directory": "${workspace_dir}",
         "environment": {
           "PYTHONPATH": "${workspace_dir}"
         }
       }
     }
   }
   ```

4. **Configure Extensões de IA**:
   - Instale a extensão "AI Assistant" se disponível
   - Configure para reconhecer o contexto do projeto Python

#### Uso:

1. Use `Cmd+Shift+P` (ou `Ctrl+Shift+P` no Windows) para abrir a paleta de comandos
2. Selecione "Run Task" e escolha a tarefa desejada
3. Use o assistente de IA para ajudar a interpretar resultados ou modificar configurações
4. O painel de saída mostrará o progresso da conversão

### Trae

[Trae](https://trae.ai/) é uma IDE agêntica focada em produtividade e assistência por IA.

#### Configuração Inicial:

1. **Importe o Projeto**:
   - Abra Trae e selecione "Open Project"
   - Navegue até o diretório do Book2MD

2. **Configure o Ambiente Python**:
   - No terminal integrado:
   ```bash
   python -m venv venv
   source venv/bin/activate  # ou venv\Scripts\activate no Windows
   pip install -r requirements.txt
   ```

3. **Crie Ações Personalizadas**:
   - Acesse "Settings > Custom Actions"
   - Adicione ações para comandos comuns:
   ```json
   [
     {
       "name": "Convert Files",
       "command": "python -m scripts.convert",
       "shortcut": "Alt+C"
     },
     {
       "name": "Watch Directory",
       "command": "python -m scripts.convert --watch",
       "shortcut": "Alt+W"
     }
   ]
   ```

4. **Ative Recursos de IA**:
   - Habilite "File Processing Intelligence"
   - Configure "Code Understanding" para Python

#### Uso:

1. Use os atalhos definidos ou o painel de ações para executar as tarefas
2. Pergunte ao assistente de IA sobre como modificar o comportamento do script
3. Use o assistente para ajudar a analisar os arquivos Markdown gerados
4. Peça sugestões para melhorar a qualidade da conversão

## Melhorando a Experiência com MCPs (Capacidades Baseadas em Modelo)

Para aproveitar ao máximo as IDEs agênticas, você pode instalar MCPs específicos que melhoram a integração com o Book2MD:

### MCPs Recomendados

1. **Python Language Server**:
   - Oferece autocompletar avançado e análise de código
   - Ajuda a identificar erros antes da execução

2. **Document Analyzer**:
   - Auxilia na compreensão de PDFs e ePUBs
   - Pode oferecer insights sobre a estrutura dos documentos

3. **Markdown Processor**:
   - Melhora a visualização e edição dos arquivos Markdown gerados
   - Oferece formatação e preview em tempo real

4. **File System Navigator**:
   - Facilita a navegação entre os diretórios de entrada e saída
   - Oferece operações em lote para arquivos

### Instalação de MCPs

A instalação de MCPs varia conforme a IDE, mas geralmente segue estes passos:

1. Acesse o gerenciador de extensões/plugins da IDE
2. Pesquise pelo MCP desejado
3. Clique em "Instalar" ou "Ativar"
4. Configure as permissões necessárias
5. Reinicie a IDE se necessário

## Tópicos Avançados

### Comandos de Voz

Algumas IDEs agênticas suportam comandos de voz. Exemplos úteis para o Book2MD:

- "Converter todos os PDFs da pasta input"
- "Iniciar modo de observação"
- "Mostrar logs da última execução"
- "Verificar status da conversão do arquivo X"

### Personalização de Prompts

Para obter melhores resultados do assistente de IA:

1. **Seja específico sobre o arquivo**:
   - "Converter o arquivo 'livro.pdf' no diretório input"
   - "Analisar o log de erro para o arquivo 'documento.epub'"

2. **Forneça contexto**:
   - "Este é um PDF técnico com muitas tabelas e diagramas"
   - "O ePUB contém equações matemáticas e código"

3. **Solicite explicações**:
   - "Por que a conversão deste arquivo falhou?"
   - "Como posso melhorar a estrutura do Markdown gerado?"

### Automação de Fluxos de Trabalho

As IDEs agênticas podem ajudar a automatizar fluxos de trabalho complexos:

1. **Processamento em Lote**:
   - Solicite ao assistente para criar scripts que processem grupos de arquivos em lote
   - "Criar um script que converta todos os PDFs em ordem alfabética"

2. **Verificação de Qualidade**:
   - Peça ao assistente para analisar a qualidade dos arquivos Markdown gerados
   - "Verificar se todos os cabeçalhos foram convertidos corretamente"

3. **Pós-processamento**:
   - Solicite ajuda para criar scripts de pós-processamento
   - "Criar um script para corrigir tabelas mal formatadas nos arquivos Markdown"