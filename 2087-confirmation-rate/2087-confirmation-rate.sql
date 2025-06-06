# Write your MySQL query statement below
SELECT s.user_id, IFNULL(p.confirmation_rate, 0) as confirmation_rate
FROM Signups s
LEFT JOIN (
    SELECT c.user_id, ROUND(AVG(if(c.action='confirmed', 1, 0)), 2) as confirmation_rate
    FROM Confirmations c
    GROUP BY c.user_id
) p
ON s.user_id = p.user_id