# Load_data

O container Load_data é o responsável por realizar buscas na api externa yfinance, ele pode ser acionada pelo container Sherherd, mas pode ser acionadao por qualquer requisição em `/load`, o `/load` é um rota POST que recebe como parâmetro o nome do ticker a ser buscado no yfinance assim com uma data inicial e data final, após realizar a busca, o load_data popula o banco de dados 3_db, a api ainda utiliza um hahs feito com a Data do preço do ticker, ele verificar esse hahs para evitar de cadastrar datas repetidas no banco de dados.

## Funcionalidade

1. **Batida na API yfinance**:
   - A API do yfinance é chamada via e os dados utilizado são retornados por `yfinance.download()`.
   - Os paraâmetros que a api recebe são repassadas para o yfinance em start_date e end_date para filtrar a busca.

2. **Salvamento no Banco de Dados**:
   - O script se conecta a um banco de dados PostgreSQL utilizando `psycopg2`.
   - Executa uma query para salvar os dados no 3_db.

### Estrutura do `.env`

O arquivo `.env` é utilizado para configurar variáveis de acesso ao banco 3_db:

```env
DB_HOST=3_db
DB_PORT=5432
DB_NAME=db
DB_USER=user
DB_PASSWORD=password
```

## Instalação

1. **Crie um ambiente virtual**:
    - ``` python -m venv .venv ```

2. **Instale as dependencias**:
    - ``` pip install -r requirements.txt ```

3. **Execute a aplicação**:
    - ```uvicorn main:app --reload```
