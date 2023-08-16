-- lists all the cities of california that can be found in the database hbtn_0d_usa
-- the states table contains only on record where name = california
-- Results will be sorted in ascending order by cities.id
-- The database name will be passed as an argument of the mysql command
SELECT id, name FROM cities
    WHERE state_id =
        (SELECT id FROM states
            WHERE name = "California")
    ORDER BY cities.id ASC;
