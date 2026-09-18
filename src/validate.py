import pandas as pd

print("Validation Started")

sales = pd.read_csv(
    "../data/staging/sales_stg.csv"
)
products = pd.read_csv(
    "../data/staging/products_stg.csv"
)
customers = pd.read_csv(
    "../data/staging/customers_stg.csv"
)
print("\nSALES CHECKS")

print(
    "Duplicate SaleID:",
    sales["SaleID"].duplicated().sum()
)

print(
    "Null SalesAmount:",
    sales["SalesAmount"].isnull().sum()
)

print(
    "Null Quantity:",
    sales["Quantity"].isnull().sum()
)

print("\nPRODUCT CHECKS")

print(
    "Duplicate ProductID:",
    products["ProductID"].duplicated().sum()
)

print("\nCUSTOMER CHECKS")

print(
    "Duplicate CustomerID:",
    customers["CustomerID"].duplicated().sum()
)

print("\nValidation Completed")