# Shepherd

O container Shepherd realiza batidas ao load_data e faz uma consulta a um banco de dados PostgreSQL a cada 7 dias. Ao realizar a batida na api load_data ele executa o endpoint `/load` que faz o carregamento dados atualizados da api Yfinance. Ao consultar o banco ele verifica a necessidade de realizar o Fine tunning, caso seja necessário ele executa o mesmo através do endpoint `/fine_tunning` e a partir desse momento o processo de fine tunning é executado sobre responsabilidade do nn_estimator.

## Funcionalidade

1. **Batida na API**:
   - A API `load_data` é chamada via HTTP POST para o endpoint `/load`.
   - Envia dois parâmetros no corpo da requisição: `start_date` (data de 1 dias atrás) e `end_date` (data do dia de hoje).
   - O horário das requisições é sempre definido como "meia-noite e um minuto" (`00:01`).

### Estrutura do `.env`

O arquivo `.env` é utilizado para configurar variáveis de acesso ao banco de redefinição do tempo de intervalo para execução do script :

```env
DAYS_INTERVAL=7
API_URL=http://2_load_data:8000
NN_API_URL=http://4_nn_estimator:8000
NN_ESTIMATOR_NAME=estimator1
DB_HOST=3_db
DB_PORT=5432
DB_NAME=db
DB_USER=user
DB_PASSWORD=password
TICKER=MSFT
```

## Instalação

1. **Crie um ambiente virtual**:
    - ``` python -m venv .venv ```

2. **Instale as dependencias**:
    - ``` pip install -r requirements.txt ```

3. **Execute a aplicação**:
    - ```python main.py```




