-- Import the database dump from hbtn_0d_tvshows to MySQL server
-- lists all shows contained in hbtn_0d_tvshows
-- Each record is displayed as: tv_shows.title - tv_show_genres.genre_id
-- Results is sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- If a show doesn't have a genre, display NULL
-- The database name will be passed as an argument of the mysql command
SELECT title, tv_show_genres.genre_id
    FROM tv_shows
    LEFT JOIN tv_show_genres
    ON tv_shows.id = tv_show_genres.show_id
    ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
