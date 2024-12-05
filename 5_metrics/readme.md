# Metrics

O container Metrics é uma api que retorna o algumas métricas referente ao modelo e sua utilização, sendo essas métricas o MSE dos dados que o modelo já tem o valor fechado, comparando com dados que ele previu para a mesma data, o data drift medido através do teste de Kolmogorov-Smirnov, assim como o tempo médio de inferencia, medido através de um log no 4_prometheus

## Funcionalidade

1. **Batida na API **:
   - A api 5_metricas possui um endpoint GET `/metrics` que não recebe nenhum parâmetro, mas retorna um json com a métricas medidas no momento a requisição.

2. **Resposta do modelo **:
   - A api retorna as métricas medidas no seguinte formato: 
```bash
{
    "mse": "0.05780089541281958",
    "data_drift": {
        "ks_statistic": "0.9844134536505332",
        "p_value": "0.00000000000000014446",
        "drift_detected": true
    },
    "avg_time_inference": null
}
```

### Estrutura do `.env`

O arquivo `.env` é utilizado para configurar variáveis de acesso ao banco 3_db e ao prometheus:

```env
DB_HOST=3_db
DB_PORT=5432
DB_NAME=db
DB_USER=user
DB_PASSWORD=password
PROMETHEUS_URL=http://4_prometheus:9090
```

## Instalação

1. **Crie um ambiente virtual**:
    - ``` python -m venv .venv ```

2. **Instale as dependencias**:
    - ``` pip install -r requirements.txt ```

3. **Execute a aplicação**:
    - ```uvicorn main:app --reload```
