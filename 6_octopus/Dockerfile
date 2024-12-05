FROM node:18-alpine AS builder

WORKDIR /usr/src/app

COPY package.json yarn.lock ./

RUN yarn install --frozen-lockfile --network-timeout 600000

COPY . .

RUN yarn build

FROM node:18-alpine AS production

WORKDIR /usr/src/app

COPY --from=builder /usr/src/app/package.json /usr/src/app/yarn.lock ./
COPY --from=builder /usr/src/app/.next /usr/src/app/.next
COPY --from=builder /usr/src/app/public /usr/src/app/public

RUN yarn install --production --frozen-lockfile --network-timeout 600000

ENV NEXT_PUBLIC_API_MODEL=http://4_api:8000/predict
ENV NEXT_PUBLIC_API_METRICS=http://5_metrics:8000/metrics

EXPOSE 3000

CMD ["yarn", "next", "start"]
