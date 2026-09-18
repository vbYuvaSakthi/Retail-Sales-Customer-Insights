CREATE TABLE dim_customers (
    CustomerID VARCHAR(20) PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Gender VARCHAR(20),
    Region VARCHAR(50)
);

CREATE TABLE dim_products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    Category VARCHAR(100)
);

CREATE TABLE dim_date (
    DateKey INT PRIMARY KEY,
    Date DATE,
    Year INT,
    Quarter INT,
    Month INT,
    MonthName VARCHAR(20)
);

CREATE TABLE dim_region (
    RegionID INT PRIMARY KEY,
    RegionName VARCHAR(100)
);