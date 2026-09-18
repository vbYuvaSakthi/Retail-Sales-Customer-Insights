-- Total Revenue
SELECT
SUM(SalesAmount) AS Total_Revenue
FROM fact_sales;

-- Total Products

SELECT ProductID,
       SUM(Quantity)
FROM fact_sales
GROUP BY ProductID;
-- Total Orders
SELECT
COUNT(*) AS Total_Orders
FROM fact_sales;

  -- Avg transaction values
  SELECT
ROUND(
AVG(SalesAmount),2
) AS Avg_Transaction_Value
FROM fact_sales;

-- Revenue by category
SELECT
dp.Category,
SUM(fs.SalesAmount) Revenue
FROM fact_sales fs
JOIN dim_products dp
ON fs.ProductID=dp.ProductID
GROUP BY dp.Category;

-- customer lifetime value
SELECT
dc.CustomerID,
CONCAT(
dc.FirstName,' ',
dc.LastName
) AS CustomerName,

SUM(fs.SalesAmount) CLV

FROM fact_sales fs
JOIN dim_customers dc
ON fs.CustomerID=dc.CustomerID

GROUP BY
dc.CustomerID,
CustomerName

ORDER BY CLV DESC;

-- Regional sales
SELECT
dc.Region,
SUM(fs.SalesAmount) Revenue

FROM fact_sales fs
JOIN dim_customers dc
ON fs.CustomerID=dc.CustomerID

GROUP BY dc.Region
ORDER BY Revenue DESC;

-- Monthly revenue Trend
SELECT
dd.Year,
dd.MonthName,
SUM(fs.SalesAmount) Revenue
FROM fact_sales fs
JOIN dim_date dd
ON fs.DateKey=dd.DateKey

GROUP BY
dd.Year,
dd.Month,
dd.MonthName

ORDER BY
dd.Year,
dd.Month;