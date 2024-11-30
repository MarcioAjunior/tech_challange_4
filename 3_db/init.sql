CREATE TABLE lb_nn_estimator (
    id SERIAL PRIMARY KEY,
    name VARCHAR(15) NOT NULL,
    status VARCHAR(15) NOT NULL,
    update_at TIMESTAMP DEFAULT NOW()
);

insert into lb_nn_estimator(name, status) values('estimator1','active');

CREATE TABLE lb_tickers_data (
    hash TEXT PRIMARY KEY,
    ticker TEXT NULL,
    date TIMESTAMP WITH TIME ZONE NOT NULL,
    open NUMERIC(12, 6) NOT NULL,
    high NUMERIC(12, 6) NOT NULL,
    low NUMERIC(12, 6) NOT NULL,
    close NUMERIC(12, 6) NOT NULL,
    volume BIGINT NOT NULL,
    price NUMERIC(12, 6) NULL,
    predicted NUMERIC(12,6) NULL,
    is_training BOOL default false
);
