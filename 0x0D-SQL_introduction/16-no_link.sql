-- lists all records of the table second_table
-- list rows without a name value is not listed
-- records are displayed in descending order of score
-- the database name will be passed as an argument to the mysql command
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
