# Write your MySQL query statement below
WITH LagFeatData AS
(
    SELECT
        id,
        recordDate,
        temperature,
        LAG(temperature, 1) OVER (ORDER BY recordDate) AS PrevDayTemp,
        LAG(recordDate, 1) OVER (ORDER BY recordDate) as PrevDate
    FROM
        Weather
)
SELECT
    id
FROM
    LagFeatData
WHERE
    temperature > PrevDayTemp
    AND
    recordDate = DATE_ADD(prevDate, INTERVAL 1 DAY)