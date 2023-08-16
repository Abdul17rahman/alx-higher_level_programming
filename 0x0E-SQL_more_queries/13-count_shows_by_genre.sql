-- Import the database dump from hbtn_0d_tvshows to MySQL server
-- lists all genres from hbtn_0d_tvshows and display the number of shows linked to each
-- each record should display: <TV Show genre> - <Number of shows linked to this genre>
-- first column must be called genre
-- second column must be called number_of_shows
-- Don't display a genre that doesn't have any shows linked
-- Results must be sorted in descending order by the number of shows linked
-- Only on SELECT statement is allowed
-- The database name will be passed as an argument of the mysql command
SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows
    FROM tv_show_genres
    RIGHT JOIN tv_genres
    ON tv_genres.id = tv_show_genres.genre_id
        WHERE tv_show_genres.genre_id IS NOT NULL
    GROUP BY tv_genres.id, genre_id
    ORDER BY number_of_shows DESC;
