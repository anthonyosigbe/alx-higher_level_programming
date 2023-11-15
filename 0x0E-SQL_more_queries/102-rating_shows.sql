-- Displays all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Records are ordered by descending rating.

SELECT s.title, IFNULL(SUM(r.rate), 0) AS rating
FROM tv_shows s
LEFT JOIN tv_show_ratings r ON s.id = r.show_id
GROUP BY s.title
ORDER BY rating DESC;
