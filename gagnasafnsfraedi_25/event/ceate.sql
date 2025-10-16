CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    name VARCHAR(1000) UNIQUE,
    date VARCHAR(10),
    location VARCHAR(1000),
    description VARCHAR(5000),
    ticket_price INTEGER,
    time VARCHAR(50),
    tickets_available INTEGER
);

CREATE TABLE tickets (
    id SERIAL PRIMARY KEY,
    event_id INTEGER,
    attendee_id INTEGER,
    purchase_date VARCHAR,
    payment_status VARCHAR(50),
    seat_number VARCHAR(1000) UNIQUE
);

CREATE TABLE attendees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(1000),
    email VARCHAR(1000) UNIQUE,
    phone_number VARCHAR(15) UNIQUE,
    account_created VARCHAR(1000)
);

CREATE TABLE organizers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(1000),
    email VARCHAR(1000) UNIQUE,
    phone_number VARCHAR(15) UNIQUE
);