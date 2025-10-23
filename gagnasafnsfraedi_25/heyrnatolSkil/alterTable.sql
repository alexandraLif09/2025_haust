ALTER TABLE headphones
ADD CONSTRAINT fk_producer
FOREIGN KEY (producersid) REFERENCES producers(id);