import pandas as pd
from sqlalchemy import create_engine
import sqlite3
from pathlib import Path

# ---------- CONFIG ----------
db_path = Path(__file__).parent / "flipkart_products.db"
csv_path = Path(__file__).parent / "flipkart_product_data.csv"
table_name = "products"


### For MySQL Configuration (if needed) ###
MYSQL_USER = "root"
MYSQL_PASSWORD = ""       # empty by default in XAMPP
MYSQL_HOST = "localhost"
MYSQL_PORT = "3306"
MYSQL_DB = "flipkart_db"
TABLE_NAME = "products"

# ---------- READ CSV ----------
df = pd.read_csv(csv_path)

# ---------- CLEAN DATA ----------
df["marked_price"] = pd.to_numeric(df["marked_price"], errors="coerce")
df["price"] = pd.to_numeric(df["price"], errors="coerce")
df["discount"] = pd.to_numeric(df["discount"], errors="coerce")
df["avg_rating"] = pd.to_numeric(df["avg_rating"], errors="coerce")
df["total_ratings"] = pd.to_numeric(df["total_ratings"], errors="coerce")

# ---------- CREATE DATABASE ----------
engine = create_engine(f"sqlite:///{db_path}")

# ---------- LOAD TO SQL ----------
df.to_sql(
    table_name,
    engine,
    if_exists="append",   # use "append" if adding more data
    index=False
)

print("✅ CSV successfully converted to SQL database!")

# ---------- MySQL Version (if needed) ----------
mysql_engine = create_engine(
    f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
)

# ---------- LOAD TO MYSQL ----------
df.to_sql(
    TABLE_NAME,
    mysql_engine,
    if_exists="append",   # use "replace" for first run
    index=False
)

print("✅ CSV successfully imported into XAMPP MySQL!")