-- My genres

SELECT tv_genres.name FROM tv_genres
	LEFT JOIN tv_show_genres
	ON tv_show_genres.genre_id=tv_genres.id
	WHERE tv_show_genres.show_id=
	(SELECT id FROM tv_shows WHERE tv_shows.title='Dexter')
	ORDER BY tv_genres.name ASC;
