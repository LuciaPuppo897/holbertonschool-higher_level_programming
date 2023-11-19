-- Write a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- task 10
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows ts
JOIN tv_show_genres tvg ON ts.id = tvg.show_id
ORDER BY ts.title ASC, tvg.genre_id ASC;