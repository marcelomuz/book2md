# Perguntas Frequentes (FAQ)

## Questões Gerais

### O que é o Book2MD?
Book2MD é uma ferramenta para conversão automática de arquivos PDF e ePUB para formato Markdown estruturado. O script utiliza o Docling como conversor principal, com fallback para o Calibre em arquivos ePUB.

### Quais são os formatos suportados?
Atualmente, o Book2MD suporta os seguintes formatos de entrada:
- PDF (.pdf)
- ePUB (.epub)

O único formato de saída é Markdown (.md).

### O Book2MD é gratuito?
Sim, o Book2MD é um projeto de código aberto distribuído sob a licença MIT, o que significa que você pode usá-lo, modificá-lo e distribuí-lo livremente.

### Preciso ter conhecimentos avançados para usar o Book2MD?
Não necessariamente. Conhecimentos básicos de linha de comando são úteis, mas a documentação fornece instruções passo a passo para uso. Se você estiver confortável em executar comandos simples no terminal, conseguirá usar o Book2MD.

## Requisitos e Instalação

### Quais são os requisitos para usar o Book2MD?
Você precisa ter:
- Python 3.7 ou superior
- Pip (gerenciador de pacotes Python)
- Calibre (para conversão de fallback de ePUBs)
- Acesso à linha de comando

### Como instalo o Calibre?
O Calibre pode ser instalado a partir do site oficial:
- Windows: [Download Calibre for Windows](https://calibre-ebook.com/download_windows)
- macOS: [Download Calibre for macOS](https://calibre-ebook.com/download_osx)
- Linux: Use o gerenciador de pacotes da sua distribuição ou siga as instruções em [calibre-ebook.com](https://calibre-ebook.com/download_linux)

### Como verifico se o Calibre está corretamente instalado?
Execute o comando abaixo no terminal:
```bash
ebook-convert --version
```
Se o comando retornar a versão do Calibre, a instalação está correta.

### O Book2MD funciona no Windows, macOS e Linux?
Sim, o Book2MD é multiplataforma e funciona em todos os sistemas operacionais que suportam Python e Calibre.

## Uso e Configuração

### Como faço para converter vários arquivos de uma vez?
Coloque todos os arquivos no diretório de entrada (ou em suas subpastas) e execute:
```bash
python -m scripts.convert
```
O script processará todos os arquivos PDF e ePUB encontrados.

### O que é o modo de observação (watch mode)?
O modo de observação mantém o script rodando continuamente, monitorando o diretório de entrada. Quando novos arquivos são adicionados, eles são automaticamente convertidos. Para ativar:
```bash
python -m scripts.convert --watch
```

### Como personalizo os diretórios de entrada e saída?
Você pode definir os diretórios de duas maneiras:
1. Editando o arquivo `.env` com as variáveis de ambiente:
   ```
   BOOK2MD_INPUT_DIR=/caminho/para/entrada
   BOOK2MD_OUTPUT_MD=/caminho/para/saida/md
   BOOK2MD_OUTPUT_LOGS=/caminho/para/saida/logs
   ```
2. Editando o arquivo `config/config.yml`:
   ```yaml
   input_dir: "/caminho/para/entrada"
   output_md: "/caminho/para/saida/md"
   output_logs: "/caminho/para/saida/logs"
   ```

### Posso converter apenas um arquivo específico?
Atualmente, o script processa todos os arquivos no diretório de entrada. Se você deseja converter apenas um arquivo específico, coloque-o sozinho em um diretório temporário e configure esse diretório como entrada.

### É possível integrar o Book2MD em outros scripts ou aplicações?
Sim, o código é modular e pode ser adaptado para uso em outros projetos Python. A função `process_file()` pode ser importada e usada de forma independente.

## Resolução de Problemas

### Por que meus PDFs não estão sendo convertidos corretamente?
Alguns problemas comuns incluem:
- PDFs com proteção ou senha
- PDFs que são apenas imagens escaneadas sem OCR
- PDFs com layouts complexos (múltiplas colunas, tabelas extensas)
- PDFs com caracteres especiais ou fontes incomuns

### O que significa o erro "calibre_fail"?
Este erro indica que o fallback para o Calibre também falhou ao tentar converter um arquivo ePUB. Possíveis causas:
- O Calibre não está instalado corretamente
- O comando `ebook-convert` não está no PATH do sistema
- O arquivo ePUB está corrompido ou protegido por DRM

### Como resolvo problemas de permissão?
Verifique se o usuário que está executando o script tem permissões de leitura nos diretórios de entrada e permissões de escrita nos diretórios de saída. Em sistemas Unix:
```bash
chmod -R 755 /caminho/para/diretorio/input
chmod -R 755 /caminho/para/diretorio/output
```

### O que fazer se o script travar ou demorar muito?
Para arquivos muito grandes ou complexos, o processo pode demorar. Se o script travar:
1. Interrompa a execução (Ctrl+C)
2. Tente processar arquivos menores ou menos complexos
3. Aumente os recursos do sistema (memória, CPU)
4. Verifique os logs para identificar o problema específico

### O número de páginas no log está incorreto. Por quê?
O número de páginas é uma estimativa baseada na contagem de cabeçalhos de nível 1 (`# `) no documento Markdown gerado. Não é uma contagem exata de páginas físicas e pode variar dependendo da estrutura do documento original.

## Qualidade da Conversão

### Como posso melhorar a qualidade da conversão?
Para obter melhores resultados:
- Use PDFs bem estruturados com texto pesquisável
- Prefira ePUBs sem DRM e bem formatados
- Certifique-se de que o Calibre está atualizado
- Considere pré-processar documentos complexos (ex: simplificar layouts)

### O Book2MD preserva imagens dos documentos?
Não, atualmente o Book2MD extrai apenas o texto e a estrutura dos documentos, convertendo para Markdown plano. Imagens não são preservadas na conversão.

### As tabelas são preservadas na conversão?
O Docling tenta preservar tabelas simples, mas tabelas complexas podem não ser convertidas corretamente. A conversão de tabelas para o formato Markdown é um desafio técnico devido às limitações do próprio formato Markdown.

### O que acontece com links, rodapés e referências?
- Links: Geralmente são preservados como links Markdown (`[texto](url)`)
- Rodapés: Podem ser convertidos para o formato Markdown de rodapé, mas com possíveis limitações
- Referências: Texto é preservado, mas o formato pode variar

## Uso Avançado

### Posso usar o Book2MD com ferramentas de automação como cron?
Sim, o Book2MD é adequado para automação. Exemplo de configuração de cron para executar a cada hora:
```
0 * * * * cd /caminho/para/book2md && /caminho/para/python -m scripts.convert
```

### Posso processar documentos em lote a partir de um script?
Sim, você pode criar scripts shell ou Python para processar documentos em lote. Exemplo de script shell:
```bash
#!/bin/bash
for dir in /caminho/base/*/; do
  export BOOK2MD_INPUT_DIR="$dir"
  export BOOK2MD_OUTPUT_MD="/caminho/saida/$(basename "$dir")"
  cd /caminho/para/book2md
  python -m scripts.convert
done
```

### Como faço para contribuir com o desenvolvimento do Book2MD?
1. Faça um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Faça commit das mudanças (`git commit -am 'Adicionei MinhaFeature'`)
4. Faça push para a branch (`git push origin feature/MinhaFeature`)
5. Crie um Pull Request

### É possível estender o Book2MD para suportar outros formatos?
Sim, o código foi projetado para ser extensível. Para adicionar suporte a novos formatos:
1. Atualize a constante `SUPPORTED_EXT` com as novas extensões
2. Implemente um conversor para o novo formato
3. Adicione lógica de fallback conforme necessário