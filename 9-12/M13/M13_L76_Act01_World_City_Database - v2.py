# ---- PART 1: Create the Table with Constraints ----
# SQL constraints are rules written inside CREATE TABLE.

import sqlite3
import pandas as pd

conn = sqlite3.connect(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M13\cities.db")

conn.execute("DROP TABLE IF EXISTS City;")

conn.execute("""
CREATE TABLE City (
    City_Id    INTEGER  PRIMARY KEY,
    City_Name  TEXT     NOT NULL UNIQUE,
    Country    TEXT     NOT NULL,
    Population INTEGER,
    Is_Capital TEXT     DEFAULT 'No'
);
""")
conn.commit()
print("Table created successfully!")

# ---- PART 2: INSERT — Adding Rows to the Table ----
conn.execute("INSERT INTO City VALUES (1, 'Tokyo',     'Japan',      13960000, 'Yes');")

conn.execute("INSERT INTO City VALUES (2, 'Nairobi',   'Kenya',       4397000, 'Yes');")

conn.execute("INSERT INTO City VALUES (3, 'Mumbai',    'India',      20667656, 'No');")

conn.execute("INSERT INTO City VALUES (4, 'Sao Paulo', 'Brazil',     12325232, 'No');")

conn.execute("INSERT INTO City VALUES (5, 'London',    'UK',          9541000, 'Yes');")

conn.execute("INSERT INTO City (City_Id, City_Name, Country) VALUES (6, 'Sydney', 'Australia');")

conn.commit()
print("Rows inserted successfully!")

cities = pd.read_sql("SELECT * FROM City;", conn)
print(cities)

# ---- PART 3: PRIMARY KEY in Action ----
# PRIMARY KEY uniquely identifies every row.
# No two rows can share the same City_Id.
# The column also cannot be NULL.
# Trying to insert a duplicate PRIMARY KEY raises an error.

print("\n--- Testing PRIMARY KEY ---")
try:
    conn.execute("INSERT INTO City VALUES (1, 'Cairo', 'Egypt', 21323000, 'Yes');")
    conn.commit()
except Exception as e:
    conn.rollback()
    print("Rejected:", e)
    print("City_Id 1 already belongs to Tokyo — PRIMARY KEY must be unique.")

# ---- PART 4: NOT NULL and UNIQUE in Action ----

print("\n--- Testing NOT NULL ---")
try:
    conn.execute("INSERT INTO City VALUES (7, 'Berlin', NULL, 3645000, 'Yes');")
    conn.commit()
except Exception as e:
    conn.rollback()
    print("Rejected:", e)
    print("Country is NOT NULL — every row must provide a country value.")

print("\n--- Testing UNIQUE ---")
try:
    conn.execute("INSERT INTO City VALUES (8, 'Tokyo', 'Japan', 99999, 'No');")
    conn.commit()
except Exception as e:
    conn.rollback()
    print("Rejected:", e)
    print("City_Name is UNIQUE — 'Tokyo' is already in the table.")

conn.close()