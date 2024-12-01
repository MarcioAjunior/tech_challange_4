FROM postgres:15-alpine

ENV POSTGRES_USER=user \
    POSTGRES_PASSWORD=password \
    POSTGRES_DB=db

COPY ./3_db/data /var/lib/postgresql/data

COPY ./3_db/init /docker-entrypoint-initdb.d/init.sql

RUN chown -R postgres:postgres /var/lib/postgresql/data

EXPOSE 5432
