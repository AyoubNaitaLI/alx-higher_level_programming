-- shownig title, genre and id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
GROUP BY tv_shows.title, tv_show_genres.genre_id
HAVING COUNT(tv_show_genres.genre_id) > 0
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
