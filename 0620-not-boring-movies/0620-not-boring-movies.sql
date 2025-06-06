# Write your MySQL query statement below
SELECT *
FROM cinema
WHERE id%2=1 AND NOT LOCATE("boring", description, 1)
ORDER BY rating DESC