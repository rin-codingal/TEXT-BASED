import sqlite3
import pandas as pd

conn = sqlite3.connect(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M13\database-6.sqlite")

print("Opened data successfully")

tables = pd.read_sql("""SELECT * 
                    FROM sqlite_master
                    WHERE type='table';""", conn)
tables

# Aliasing 
match_details = pd.read_sql('''SELECT Season_Id, Match_Id,  
                              v.Venue_Name, c.City_Name, t.Team_Name AS Winner 
                              FROM Match
                              INNER JOIN Venue AS v ON match.Venue_Id == v.Venue_Id
                              INNER JOIN City AS c ON v.City_Id == c.City_Id
                              INNER JOIN Team AS t ON match.Match_Winner == t.Team_Id;''', conn)

match_details
