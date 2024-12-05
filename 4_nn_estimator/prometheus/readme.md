# NN estimator promethes

O container NN prometheus apenas contem uma pesonalização na configuração do container para coletar as métrica de inferencia realizadas pela api.

## Funcionalidade

1. **Batida na API**:
   - É possível acessar as métricas padrões do promethues assim como tempo médio de inferencia ao acessar o container na http://4_prometheus/ ou ainda através de uma porta bindadad no docker-compose.yaml

## Query

    - A query necessária para verificar o tempo médio de inferencia
    - ``` model_inference_time_seconds_sum / model_inference_time_seconds_count ```