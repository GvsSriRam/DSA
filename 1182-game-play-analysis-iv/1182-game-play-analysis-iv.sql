# Write your MySQL query statement below
WITH SecondDates AS (
    SELECT player_id, DATE_ADD(min(event_date), INTERVAL 1 day) as second_date
    FROM Activity
    GROUP BY player_id
),

consec_logins AS (
    SELECT COUNT(a.player_id) as num_logins
    FROM Activity a
    INNER JOIN SecondDates s
    ON a.player_id = s.player_id AND a.event_date = s.second_date
)

SELECT ROUND(
    (SELECT c.num_logins FROM consec_logins c) / (SELECT COUNT(s.player_id) FROM SecondDates s)
    , 2
)
AS fraction
