import sqlite3
import pandas as pd

conn = sqlite3.connect(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M13\database-2.sqlite")

print("Opened data successfully")

# Read SQL query for getting all the tables of database into a dataframe
tables = pd.read_sql("""SELECT * 
                    FROM sqlite_master
                    WHERE type='table';""", conn)
tables

# Read Table from the database into dataframe
matches = pd.read_sql("""SELECT *
                        FROM Match;""", conn)

# Print Table info
matches.info()