INSERT INTO pizzas (name, description, price)
VALUES ('Margherita', 'sósa og ostur', 50000),
('Pepperoni', 'sósa, ostur og pepperoni', 60000),
('Vegan Delight', 'sósa, vegan ostur, sveppir, papriku og laukur', 70000),
('Hawaiian', 'sósa, ostur, skinka og ananas', 65000),
('BBQ Chicken', 'BBQ sósa, ostur og kjúklingur', 75000);

SELECT * FROM pizzas;

INSERT INTO ingredients (name, portionSize, price, isVegan)
VALUES 
('pizza sósa', 20,10, TRUE),
('ostur', 50, 10000, FALSE),
('pepperoni', 30, 250, FALSE),
('vegan ostur', 50, 12000, TRUE),
('skinka', 40, 13000, FALSE),
('ananas', 30, 8000, TRUE),
('kjúklingur', 50, 14000, FALSE),
('sveppir', 20, 300, TRUE),
('paprika', 20, 300, TRUE),
('laukur', 20, 6000, TRUE);

SELECT * FROM ingredients;

INSERT INTO pizzaIngredients (idPizza, idIngredient)
VALUES (1, 1), -- Margherita - pizza sósa
(1, 2), -- Margherita - ostur
(2, 1), -- Pepperoni - pizza sósa
(2, 2), -- Pepperoni - ostur
(2, 3), -- Pepperoni - pepperoni
(3, 1), -- Vegan Delight - pizza sósa
(3, 4), -- Vegan Delight - vegan ostur
(3, 8), -- Vegan Delight - sveppir
(3, 9), -- Vegan Delight - paprika
(3, 10), -- Vegan Delight - laukur
(4, 1), -- Hawaiian - pizza sósa
(4, 2), -- Hawaiian - ostur
(4, 5), -- Hawaiian - skinka
(4, 6), -- Hawaiian - ananas
(5, 7), -- BBQ Chicken - kjúklingur
(5, 1), -- BBQ Chicken - pizza sósa
(5, 2); -- BBQ Chicken - ostur

SELECT * FROM pizzaIngredients;

INSERT INTO customers (firstName,lastName, email, phone, address)
VALUES ('Jón', 'Sigurðsson', 'js@fb.is', '5554950', 'Beljuland'),
('Karl', 'Magnússon', 'km@fb.is', '55524876', 'Dúfnahólar'),
('Alexandra Líf', 'Adolphssdóttir','alexadolph@gmail.com', '5552343', 'Tinnuberg');

SELECT * FROM customers;

INSERT INTO pizzaOrders (idPizza, idCustomer)
VALUES (3, 2);

SELECT * FROM pizzaOrders;