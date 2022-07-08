-- imported database
-- scripts lists all generes of a database
SELECT tv_shows.title, tv_shows_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.shows_id
LEFT JOIN tv_genres ON tv_shows_genres.genre_id = tv_genres.id
ORDER BY tv_show.title, tv_genres.name;
