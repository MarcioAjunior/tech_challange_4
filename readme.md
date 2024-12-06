# Tech challange fase 4

O presente repositório trata-se da entrega do Tech Challange fase 4 do curso de pós graduação Machine Learning Engineering do grupo 45. O trabalho apresenta uma arquitetura criada para atender os requisitos da atividade proposta
    - Coleta e pré processamento de dados.
    - Desenvolvimento de um modelo LSTM.
    - Salvamento e exportação do modelo.
    - Deploy do modelo.
    - Escalabilidade e monitoramento.

## Escolha da ação

Para a realização do trabalho, foi escolhida a ação da Microsoft, representada pelo ticker `MSFT` da api do yfinance, além disso foi definida uma arquitetura e uma rotina de funcionamento para a arquitetura.


## Arquitetura

A arquitetura dos serviços é representada visualmente pela imagem abaixo

![Arquitetura](./arch.png)

Onde :

1. **1_shepherd**:
   - É um script agendado, que roda perioódicamente para realizar novamente a tarefa de extração de dados. Além disso é reponsável por verificar a necessidade de realizar fine tunning no modelo novamente, comaparando a data dos registros atuais com os ultimos registro salvos no banco, quando a diferença for maior que o periodo estipulado pelo shepherd é realizada nova extração de dados e fine tunning para atualizar o modelo.
   - [Mais detalhes sobre o shepheard ](./1_shepherd/)

2. **2_load_data**:
   - É uma api feita em fastApi para interação com o a api externa a arquitetura Yfinance, ela é responsável realizar busca na api yfinance, utilizando-se de parâmetros informados na requisição, sendo eles
     - ticket
     - start_date
     - end_date
   - Após busca filtrada os dados são salvos no 3_db, estes dados serão posteriormente utilizadados para treinamento/validação do modelo que será exposto por 4_nn_estimator.
   - [Mais detalhes sobre o load_data ](./2_load_data/)

3. **3_db**:
   - É um banco de dados postgres configurado somente no docker-compose.yaml, utiliza-se de um script de inicizalização para criar as tabelas necessárias para o funcionamento da architetura. É onde ficam quardados os dados de treinamento, informações sobre o estimador e seu status.
   - [Mais detalhes sobre o 3_db ](./3_db/)
  
4. **4_nn_estimator_API**:
   - É a api que espoem o modelo no endpoint POST `/predict`, esse endpoint é usado pelo 6_octopus. Além disso é o container que contabiliza o tempo médio de inferencia no modelo e salva seus logs em 4_nn_estimator_prometheus;
   - [Mais detalhes sobre o 4_nn_estimator_api ](./4_nn_estimator/api/)
  
5. **4_nn_estimator_mlflow**:
   - É um container que contem os estudos realizados para desenvolvimento do modelo, ele contém as métricas e diferente artefatos e estudos que foram utilizados no desenvolvimento, esse container ainda possibilida a criação de um novo modelo quando necessário.
   - [Mais detalhes sobre o 4_nn_estimator_mlflow ](./4_nn_estimator/mlflow/)
  
6. **4_nn_estimator_prometheus**:
   - É um container que armazena o log da api de inferencia, é possível ainda acessar o container para verificar outras métricas padrão do prometheus.
   - [Mais detalhes sobre o 4_nn_estimator_prometheus ](./4_nn_estimator/prometheus/)
  
7. **5_metrics**:
   - É uma api que retorna as métrica do modelo no momento em que a requisição é realizada, está api é consumida pelo octopus para mostras essas métricas no frontend da aplicação. as métricas retornadas são MSE, data drift e tempo médio de inferencia.
   - [Mais detalhes sobre o 5_metrics ](./5_metrics/)
  
8. **6_octopus**:
   - É o frontend da aplicação feito em next e typescript, ele mostra um gráfico com os dados coletado e previsto para realizar um comparativo, além de permitir inferencia a partir de uma data.
   - [Mais detalhes sobre o 6_octopus ](./6_octopus/)
