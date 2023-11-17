-- Write a script that creates the table id_not_null on your MySQL server.
-- task 4
CREATE TABLE IF IS NOT EXISTS id_not_null (
    id INT UNIQUE 1,
    name VARCHAR(256)
);
