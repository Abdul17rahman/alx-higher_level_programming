-- creates user user_0d_1 on the MySQL server
-- user_0d_1 will have all privileges
-- The user_0d_1 password should be set to user_0d_1_pwd
-- Ignore if already exit
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
