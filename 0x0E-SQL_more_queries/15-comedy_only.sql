-- imported database
-- scripts lists all generes of a database
SELECT tv_shows.title
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.shows_id
INNER JOIN tv_genres ON tv_shows_genres.genre_id = tv_genres.id
WHERE tv_shows.name = 'Comedy'
ORDER BY tv_show.title;
