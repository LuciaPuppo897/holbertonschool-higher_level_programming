-- Write a script that lists all cities contained in the database hbtn_0d_usa.
-- task 9
SELECT cities.id, cities.name, states.name
FROM cities,states
WHERE cities.state_id = states_id
ORDER BY cities.id;