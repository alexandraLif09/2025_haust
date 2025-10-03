CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    firstName VARCHAR(255),
    lastName VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(255),
    address VARCHAR(255)
);

CREATE TABLE pizzas (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE,
    description VARCHAR(255),
    price INTEGER
);

CREATE TABLE pizzaOrders (
    id SERIAL PRIMARY KEY,
    idPizza INTEGER,
    idCustomer INTEGER
);

CREATE TABLE pizzaIngredients (
    idPizza INTEGER,
    idIngredient INTEGER
);

