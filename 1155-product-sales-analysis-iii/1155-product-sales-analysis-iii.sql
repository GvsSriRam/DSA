# Write your MySQL query statement below
WITH FirstYear AS (
    SELECT product_id, min(year) as first_year
    FROM Sales
    GROUP BY product_id
)

SELECT product_id, year as first_year, quantity, price
FROM Sales
WHERE (product_id, year) in (SELECT * FROM FirstYear)