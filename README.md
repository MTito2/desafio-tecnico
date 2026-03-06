# Desafio Técnico
Este projeto consiste em uma automação que coleta, processa e envia dados sobre países com maior média de idade da população.

O processo é dividido em quatro etapas principais:

1. **Scraping de dados**  
   A automação acessa a página do Worldometers e identifica os 10 países com maior média de idade, capturando:
   - Nome do país
   - Quantidade de habitantes
   - Média de idade

2. **Consumo de API**  
   Para cada país encontrado, é realizada uma consulta na API REST Countries para obter:
   - Capital
   - Linguagens faladas
   - Nome das moedas

3. **Consolidação dos dados**  
   As informações coletadas são combinadas e organizadas em um arquivo `.xlsx` com a seguinte estrutura:


## Estrutura do Projeto

O projeto foi organizado em módulos para separar responsabilidades e facilitar manutenção e leitura do código.

### scraping.py
Responsável por realizar o **web scraping** da tabela de países no site:

https://www.worldometers.info/world-population/population-by-country/

Esse módulo automatiza o acesso à página, extrai os dados da tabela e identifica os **10 países com maior média de idade**, coletando:
- Nome do país
- Quantidade de habitantes
- Média de idade

---

### api_client.py
Responsável por consumir a API pública:

https://restcountries.com/

Para cada país obtido no scraping, o módulo consulta a API e coleta:
- Capital
- Linguagens faladas
- Nome das moedas

---

### data_service.py
Responsável pela **consolidação dos dados**.

Esse módulo combina:
- Os dados obtidos no scraping
- As informações retornadas pela API

Gerando uma estrutura final com todas as informações necessárias para o relatório.

---

### report_generator.py
Responsável por gerar o **arquivo de saída em formato `.xlsx`**.

Esse módulo recebe os dados consolidados e cria uma planilha estruturada.

---

### webhook_client.py
Responsável por realizar o **envio do arquivo gerado** para um webhook.

O módulo realiza uma requisição **HTTP POST**, anexando a planilha gerada para envio automático.

---

### main.py
Arquivo principal do projeto.

É responsável por **orquestrar todo o fluxo da automação**, chamando as funções principais de cada módulo na seguinte ordem:

1. Executa o scraping dos países
2. Consolida as informações
3. Gera a planilha final
4. Envia o arquivo para o webhook
