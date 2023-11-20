-- Write a script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
-- task 12
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows ts
LEFT JOIN tv_show_genres tvg ON tv_shows.id = tv_show_genres.show_id
WHERE tvg.genre_id IS NULL
ORDER BY ts.title ASC, tvg.genre_id ASC;