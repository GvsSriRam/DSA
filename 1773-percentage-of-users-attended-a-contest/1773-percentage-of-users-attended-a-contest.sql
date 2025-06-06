# Write your MySQL query statement below
SELECT r.contest_id, ROUND(
    100*COUNT(DISTINCT r.user_id)/(
    SELECT COUNT(user_id) FROM Users), 
    2
) as percentage
FROM Register r
GROUP BY contest_id
ORDER BY percentage DESC, r.contest_id ASC