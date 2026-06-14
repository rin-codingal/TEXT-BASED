import sqlite3
import pandas as pd

conn = sqlite3.connect(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M13\database-4.sqlite")

print("Opened data successfully")

# Display all the tables of the database
df = pd.read_sql("""SELECT * 
                    FROM sqlite_master
                    WHERE type='table';""", conn)
df

# Display the first five rows of the Player_Match table
player_match = pd.read_sql("""SELECT *
                        FROM Player_Match""", conn)

player_match.head()

# Check the presence of null values in the Player_Match table
null_player_match = pd.read_sql("""SELECT *
                        FROM Player_Match
                        WHERE Team_Id IS NULL""", conn)

null_player_match

# Display the first five rows of the Match table
toss_dec = pd.read_sql("""SELECT *
                        FROM Match""", conn)

toss_dec.head()

# Check the presence of null values in the Match table
null_match = pd.read_sql("""SELECT *
                        FROM Match
                        WHERE MATCH_Winner IS NULL""", conn)

null_match