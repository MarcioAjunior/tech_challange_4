# Shepherd

O container Shepherd realiza batidas ao load_data e faz uma consulta a um banco de dados PostgreSQL a cada 7 dias. Ao realizar a batida na api load_data ele executa o endpoint `/load` que faz o carregamento dados atualizados da api Yfinance. Ao consultar o banco ele verifica a necessidade de realizar o Fine tunning, caso seja necessário ele executa o mesmo através do endpoint `/fine_tunning` e a partir desse momento o processo de fine tunning é executado sobre responsabilidade do nn_estimator.

## Funcionalidade

1. **Batida na API**:
   - A API `load_data` é chamada via HTTP POST para o endpoint `/load`.
   - Envia dois parâmetros no corpo da requisição: `start_date` (data de 7 dias atrás) e `end_date` (data do dia de hoje).
   - O horário das requisições é sempre definido como "meia-noite e um minuto" (`00:01`).

2. **Consulta ao Banco de Dados**:
   - O script se conecta a um banco de dados PostgreSQL utilizando `psycopg2`.
   - Executa uma query para verificar a necessida de fine tunning.
   - Executa o fine tunning quando necessário.

### Estrutura do `.env`

O arquivo `.env` é utilizado para configurar variáveis de acesso ao banco de redefinição do tempo de intervalo para execução do script :

```env
DAYS_INTERVAL=7
API_URL=https://example.com/load
DB_HOST=localhost
DB_PORT=5432
DB_NAME=mydatabase
DB_USER=myuser
DB_PASSWORD=mypassword
```

## Instalação

1. **Crie um ambiente virtual**:
    - ``` python -m venv .venv ```

2. **Instale as dependencias**:
    - ``` pip install -r requirements.txt ```

3. **Execute a aplicação**:
    - ```python main.py```




