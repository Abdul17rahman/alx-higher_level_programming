-- creates the table force_name
-- description:
--      id int
--      name VARCHAR(256) and can't be null
-- The database name will be passed as an argument of the mysql command
-- ignore if the table force_name already exists
CREATE TABLE IF NOT EXISTS force_name(id INT, name VARCHAR(256) NOT NULL);
