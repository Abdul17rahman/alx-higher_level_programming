-- lists all cities contained in the database hbtn_0d_usa
-- Results must be sorted in ascending order by cities.id
-- Only one select statement is allowed
-- The database name will be passed as an argument of the mysql command
SELECT cities.id, cities.name, states.name
    FROM cities
    INNER JOIN states
    ON states.id = cities.state_id
    ORDER BY cities.id ASC;
