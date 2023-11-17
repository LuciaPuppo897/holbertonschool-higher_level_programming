-- Write a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa)
CREATE DATEBASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXIST states(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);