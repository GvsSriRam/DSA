# Write your MySQL query statement below
WITH RepCount AS (
    SELECT managerId, count(managerId) as counts
    FROM Employee
    GROUP BY managerId
)

SELECT name
FROM Employee e
LEFT JOIN RepCount as r
ON e.id = r.managerId
WHERE r.counts>=5