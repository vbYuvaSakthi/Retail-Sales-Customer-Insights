CREATE VIEW vw_sales_analytics AS
SELECT
    fs.SaleID,
    fs.SalesID_SK,
    fs.SalesAmount,
    fs.Quantity,

    dp.ProductName,
    dp.Category,

    dc.CustomerID,
    CONCAT(dc.FirstName,' ',dc.LastName) AS CustomerName,
    dc.Gender,
    dc.Region,

    dd.Date,
    dd.Month,
    dd.MonthName,
    dd.Quarter,
    dd.Year

FROM fact_sales fs
JOIN dim_products dp
    ON fs.ProductID = dp.ProductID

JOIN dim_customers dc
    ON fs.CustomerID = dc.CustomerID

JOIN dim_date dd
    ON fs.DateKey = dd.DateKey;