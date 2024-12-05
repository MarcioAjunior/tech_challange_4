# Octopus

O octopus é o front-end da arquitetura, responsável por mostrar os dados de fechamento dos valores da ação escolhida. O octopus pemite que seja realizada inferencias no modelo ao escolher uma data de até 7 dias do ultimo dado coletado

### Estrutura do `.env`

O arquivo `.env` é utilizado para configurar variáveis de acesso ao banco 3_db e as apis de modelo e metricas:

```env
NEXT_PUBLIC_API_MODEL=http://4_api:8000/predict
NEXT_PUBLIC_API_METRICS=http://5_metrics:8000/metrics
```

## Instalação 

1. **Clone o repositório**:

2. **Instale as dependencias**:
    - ``` yarn install ``` ou ``` npm install ```

3. **Execute a aplicação**:
    - ```bash
        npm run dev
        # or
        yarn dev
        # or
        pnpm dev
        # or
        bun dev
        ```
