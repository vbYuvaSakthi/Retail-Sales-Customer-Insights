import pandas as pd
import json
import os

os.makedirs("../data/staging", exist_ok=True)
print("Starting Extraction Process...")
sales = pd.read_csv("../data/raw/sales 1.csv")
products = pd.read_csv("../data/raw/products.csv")
with open("../data/raw/customers.json", "r", encoding="utf-8") as f:
    customers = pd.DataFrame(json.load(f))
sales.to_csv(
    "../data/staging/sales_stg.csv",
    index=False
)
products.to_csv(
    "../data/staging/products_stg.csv",
    index=False
)
customers.to_csv(
    "../data/staging/customers_stg.csv",
    index=False
)
print("Extraction Completed Successfully")