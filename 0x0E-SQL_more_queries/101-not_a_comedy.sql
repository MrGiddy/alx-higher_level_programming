-- List all shows without the genre Comedy in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- You can use a maximum of two SELECT statement
SELECT DISTINCT ts.title
  FROM tv_shows AS ts
       LEFT JOIN tv_show_genres AS tsg
       ON ts.id = tsg.show_id

       LEFT JOIN tv_genres AS tg
       ON tsg.genre_id = tg.id
       WHERE ts.title NOT IN (
             SELECT ts.title
               FROM tv_shows AS ts
                    INNER JOIN tv_show_genres AS tsg
                    ON ts.id = tsg.show_id

                    INNER JOIN tv_genres AS tg
                    ON tsg.genre_id = tg.id
                    WHERE tg.name = "Comedy")
ORDER BY ts.title ASC;