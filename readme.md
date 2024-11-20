# Tech challange fase 4

O presente repositório trata-se da entrega do Tech Challange fase 4 do curso de pós graduação Machine Learning Engineering do grupo 45. O trabalho apresenta uma arquitetura criada para atender os requisitos da atividade proposta
    - Coleta e pré processamento de dados.
    - Desenvolvimento de um modelo LSTM.
    - Salvamento e exportação do modelo.
    - Deploy do modelo.
    - Escalabilidade e monitoramento.

## Arquitetura

A arquitetura dos serviços é representada visualmente pela imagem abaixo

![Arquitetura](./arch.png)

Onde :

1. **1_shepherd**:
   - É um script agendado, que roda perioódicamente para realizar novamente a tarefa de extração de dados. Além disso é reponsável por verificar a necessidade de realizar fine tunning no modelo novamente, comaparando a data dos registros atuais com os ultimos registro salvos no banco, quando a diferença for maior que o periodo estipulado pelo shepherd é realizada nova extração de dados e fine tunning para atualizar o modelo.
   - [Mais detalhes sobre o shepheard ](./1_shepherd/)

2. ****:
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




