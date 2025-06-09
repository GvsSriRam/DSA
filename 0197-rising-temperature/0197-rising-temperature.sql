# Write your MySQL query statement below
SELECT currW.id as Id
FROM Weather currW
JOIN Weather prevW
ON currW.recordDate = DATE_ADD(prevW.recordDate, INTERVAL 1 DAY)
WHERE currW.temperature > prevW.temperature