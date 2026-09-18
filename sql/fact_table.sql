CREATE TABLE fact_sales (
    SalesID_SK INT PRIMARY KEY,
    SaleID VARCHAR(50),
    ProductID INT,
    CustomerID VARCHAR(20),
    DateKey INT,
    SalesAmount DECIMAL(12,2),
    Quantity INT,

    CONSTRAINT fk_product
        FOREIGN KEY (ProductID)
        REFERENCES dim_products(ProductID),

    CONSTRAINT fk_customer
        FOREIGN KEY (CustomerID)
        REFERENCES dim_customers(CustomerID),

    CONSTRAINT fk_date
        FOREIGN KEY (DateKey)
        REFERENCES dim_date(DateKey)
);