-- Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL
SELECT score, name
WHERE name EXISTS
ORDER BY score DESC

