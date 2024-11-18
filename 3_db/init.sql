CREATE TABLE lb_nn_estimator (
    id SERIAL PRIMARY KEY,
    name VARCHAR(15) NOT NULL,
    status VARCHAR(15) NOT NULL,
    update_at TIMESTAMP DEFAULT NOW()
);
