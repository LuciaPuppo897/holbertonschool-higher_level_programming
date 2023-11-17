-- Write a script that creates the MySQL server user user_0d_1.
-- task 1
CREATE USER IF NOT EXIST user_0d_1@localhost;
SET PASSWORD FOR user_0d_1@localhost = 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO user_0d_1@localhost;
FLUSH PRIVILEGES;