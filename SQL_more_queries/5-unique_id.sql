-- Write a script that creates the table unique_id on your MySQL server.
CREATE TABLE IF IS NOT EXISTS unique_id(
    id INT = 1,
    name VARCHAR(256),
    UNIQUE (id)
);

