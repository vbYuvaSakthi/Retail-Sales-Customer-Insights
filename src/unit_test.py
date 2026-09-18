import pandas as pd

print("Running Tests...")

fact_sales = pd.read_csv(
    "../data/processed/fact_sales.csv"
)

dim_customers = pd.read_csv(
    "../data/processed/dim_customers.csv"
)

dim_products = pd.read_csv(
    "../data/processed/dim_products.csv"
)

dim_date = pd.read_csv(
    "../data/processed/dim_date.csv"
)

# -------------------------
# FACT TABLE TESTS
# -------------------------

assert len(fact_sales) > 0

assert (
    fact_sales["SalesID_SK"].is_unique
)

assert (
    fact_sales["SaleID"].isnull().sum()
    == 0
)

# -------------------------
# CUSTOMER DIMENSION TESTS
# -------------------------

assert len(dim_customers) > 0

assert (
    dim_customers["CustomerID"]
    .isnull()
    .sum()
    == 0
)

# -------------------------
# PRODUCT DIMENSION TESTS
# -------------------------

assert len(dim_products) > 0

assert (
    dim_products["ProductID"]
    .isnull()
    .sum()
    == 0
)

# -------------------------
# DATE DIMENSION TESTS
# -------------------------

assert len(dim_date) > 0

assert (
    dim_date["DateKey"]
    .is_unique
)

print("All Tests Passed Successfully")