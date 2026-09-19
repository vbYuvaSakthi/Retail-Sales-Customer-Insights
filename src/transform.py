import pandas as pd
import os

print("Transformation Started...")

# Create processed folder
os.makedirs("../data/processed", exist_ok=True)

sales = pd.read_csv(
    "../data/staging/sales_stg.csv"
)

products = pd.read_csv(
    "../data/staging/products_stg.csv"
)

customers = pd.read_csv(
    "../data/staging/customers_stg.csv"
)

# SALES CLEANING

sales.drop_duplicates(inplace=True)

sales["SalesAmount"] = sales["SalesAmount"].fillna(
    sales["SalesAmount"].median()
)

sales["Quantity"] = sales["Quantity"].fillna(
    sales["Quantity"].median()
)

sales["Timestamp"] = pd.to_datetime(
    sales["Timestamp"]
)

# Remove invalid revenue

sales = sales[
    sales["SalesAmount"] > 0
]

# Remove invalid quantity
sales = sales[
    sales["Quantity"] > 0
]

# SURROGATE KEY
sales.insert(
    0,
    "SalesID_SK",
    range(1, len(sales) + 1)
)

# DATE DIMENSION
dim_date = pd.DataFrame()

dim_date["Date"] = sales["Timestamp"].dt.date

dim_date = dim_date.drop_duplicates()

dim_date["DateKey"] = (
    pd.to_datetime(dim_date["Date"])
    .dt.strftime("%Y%m%d")
    .astype(int)
)

dim_date["Year"] = (
    pd.to_datetime(dim_date["Date"])
    .dt.year
)

dim_date["Quarter"] = (
    pd.to_datetime(dim_date["Date"])
    .dt.quarter
)

dim_date["Month"] = (
    pd.to_datetime(dim_date["Date"])
    .dt.month
)

dim_date["MonthName"] = (
    pd.to_datetime(dim_date["Date"])
    .dt.month_name()
)

# PRODUCT DIMENSION

dim_products = products.copy()

# Remove duplicate records
dim_products.drop_duplicates(
    subset=["ProductID"],
    inplace=True
)

# Remove leading/trailing spaces
dim_products["ProductName"] = (
    dim_products["ProductName"]
    .astype(str)
    .str.strip()
)

dim_products["Category"] = (
    dim_products["Category"]
    .astype(str)
    .str.strip()
)

# Fill missing values if any
dim_products["ProductName"] = (
    dim_products["ProductName"]
    .fillna("Unknown Product")
)

dim_products["Category"] = (
    dim_products["Category"]
    .fillna("Unknown Category")
)

# CUSTOMER DIMENSION

dim_customers = customers.copy()

# remove duplicate customers
dim_customers.drop_duplicates(
    subset=["CustomerID"],
    inplace=True
)

# remove SSN
if "SSN" in dim_customers.columns:
    dim_customers.drop(
        columns=["SSN"],
        inplace=True
    )

# fill LastName nulls
if "LastName" in dim_customers.columns:
    dim_customers["LastName"] = (
        dim_customers["LastName"]
        .fillna("Unknown")
    )

# fill Region nulls
if "Region" in dim_customers.columns:
    dim_customers["Region"] = (
        dim_customers["Region"]
        .fillna("Unknown")
    )

# standardize Gender

dim_customers["Gender"] = (
    dim_customers["Gender"]
    .astype(str)
    .str.upper()
)

dim_customers["Gender"] = (
    dim_customers["Gender"]
    .replace({
        "MALE": "M",
        "FEMALE": "F"
    })
)

# standardize Regions

dim_customers["Region"] = (
    dim_customers["Region"]
    .replace({
        "Ohho": "Ohio",
        "california": "California",
        "Californiya": "California",
        "NY": "New York",
        "Nw York": "New York",
        "New Yorkk": "New York",
        "Texaz": "Texas"
    })
)

# REGION DIMENSION

dim_region = pd.DataFrame()

dim_region["RegionName"] = (
    dim_customers["Region"]
)

dim_region = (
    dim_region
    .drop_duplicates()
    .reset_index(drop=True)
)

# remove Unknown region

dim_region = (
    dim_region[
        dim_region["RegionName"] != "Unknown"
    ]
)

dim_region = dim_region.reset_index(
    drop=True
)

dim_region["RegionID"] = range(
    1,
    len(dim_region) + 1
)

# FACT TABLE

sales["DateKey"] = (
    sales["Timestamp"]
    .dt.strftime("%Y%m%d")
    .astype(int)
)

fact_sales = sales[
    [
        "SalesID_SK",
        "SaleID",
        "ProductID",
        "CustomerID",
        "DateKey",
        "SalesAmount",
        "Quantity"
    ]
]

# EXPORT FILES

dim_customers.to_csv(
    "../data/processed/dim_customers.csv",
    index=False
)

dim_products.to_csv(
    "../data/processed/dim_products.csv",
    index=False
)

dim_date.to_csv(
    "../data/processed/dim_date.csv",
    index=False
)

dim_region.to_csv(
    "../data/processed/dim_region.csv",
    index=False
)

fact_sales.to_csv(
    "../data/processed/fact_sales.csv",
    index=False
)

print("\nTransformation Completed")

print("\nRows Created")

print(
    "Fact Sales:",
    len(fact_sales)
)

print(
    "Dim Customers:",
    len(dim_customers)
)

print(
    "Dim Products:",
    len(dim_products)
)

print(
    "Dim Date:",
    len(dim_date)
)

print(
    "Dim Region:",
    len(dim_region)
)

print("\nFiles Generated:")
print("dim_customers.csv")
print("dim_products.csv")
print("dim_date.csv")
print("dim_region.csv")
print("fact_sales.csv")
