-- lists the number of records with the same score in the table second_table
-- The result display:
--      the score
--      the number of records for this score with the label number
-- the list is sorted by the number of records(descending)
-- the database name will be passed as an argument to the mysql command
SELECT score, COUNT(score) AS number
    FROM second_table
        GROUP BY score
            ORDER BY number DESC;
