# NN estimator api

O container NN estimator api é responsável por armazenar o `.pth` do modelo, realizar o carregamento, do modelo, e realizar a inferencia, ele retorna a data prevista para uma data especifica de até 7 dias adiantes do ultimo valor fechado existente no banco, que é atualizado diariamente pelo shepherd. O NN estimator ainda é reponsável por salver em NN estimator promethues o tempo de inferencia de cada inferencia realizada no endpoint `/predict`  

## Funcionalidade

1. **Batida na API**:
   - A API `NN_estimator_api` é chamada via HTTP POST para o endpoint `/predict`.
   - Envia um único parâmetro date string no formato 'YYYY-mm-dd'.
   - O retorno é o resultado no máximo 10 registros sendo desses 10 no máximo 7 predições realizadas pelo modelo, isso ocorre para que possa se ter referencia história da predição para montagem do gráfico existente no octopus.


### Estrutura do `.env`

O arquivo `.env` é utilizado para configurar variáveis de acesso ao banco e acesso ao modelo :

```env
DB_HOST=3_db
DB_PORT=5432
DB_NAME=db
DB_USER=user
DB_PASSWORD=password
MODEL_PATH=./model.pth
TICKER=MSFT
```

## Instalação

1. **Crie um ambiente virtual**:
    - ``` python -m venv .venv ```

2. **Instale as dependencias**:
    - ``` pip install -r requirements.txt ```

3. **Execute a aplicação**:
    - ```uvicorn main:app --reload```
