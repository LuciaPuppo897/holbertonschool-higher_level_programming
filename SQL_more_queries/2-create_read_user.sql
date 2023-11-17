--Write a script that creates the database hbtn_0d_2 and the user user_0d_2.
CREATE DATEBASE IF NOT EXIST hbtn_0d_2;
CREATE USER IF NOT EXIST 'user_0d_2'@'localhost';
SET PASSWORD FOR user_0d_2@localhost ='user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;