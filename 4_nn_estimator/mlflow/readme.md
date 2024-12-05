# NN estimator mlflow

O container NN estimator mlflow tem como responsábilidade principal gerar e armazenar os estudos realizados pelo modelo, ele ainda guarda as métricas dos treinamentos realizados e roda através do entrypoint nativo do mlflow, para que se possa explorar os estudo através da mlflow UI. Este container não possui uma responsábilidade maio do que esta, e seria possível utilzar a arquitetura sem a existencia desse container.  

## Funcionalidade

1. **Batida na API**:
   - É possível acessar os estudos e suas métrica as acessar o contaner na rede http://4_mlflow/ após iniciar os container, ou ainda em uma porta bindade pelo docker-compose.yaml

### Estrutura do `.env`

O arquivo `.env` é utilizado para configurar variáveis de acesso ao banco e acesso ao modelo :

```env
DB_HOST=3_db
DB_PORT=5432
DB_NAME=db
DB_USER=user
DB_PASSWORD=password
FROM_DATE = None
TICKER=MSFT
```

## Instalação

1. **Crie um ambiente virtual**:
    - ``` python -m venv .venv ```

2. **Instale as dependencias**:
    - ``` pip install -r requirements.txt ```

3. **Execute a aplicação**:
    - ```mlflow ui```
