-- script lists all genres
SELECT tv_genres.name AS genre, 
COUNT(*) AS number_of_shows 
FROM tv_show_genres
JOIN tv_show_genres ON tv_generes.id = tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
