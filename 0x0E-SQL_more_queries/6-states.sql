-- creates the database hbtn_0d_usa
-- creates the table states
-- states description:
--      id int unique, auto generated, can't be null and is a primary key
--      name VARCHAR(256) can't be null
-- ignore if the database hbtn_0d_usa already exists
-- ignore table creation if the table states already exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT UNIQUE PRIMARY KEY NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL
);
