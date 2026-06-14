import sqlite3
import pandas as pd


conn = sqlite3.connect(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M13\database.sqlite")
print("Opened data successfully")

tables = pd.read_sql("SELECT * FROM sqlite_master WHERE type='table';", conn)
print(tables)