# ---- PART 1: Open the Database ----
# This database stores information about popular movies.
# It has three tables: Movie, Actor, and Movie_Actor.

import sqlite3
import pandas as pd

conn = sqlite3.connect(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M13\movies.db")

print('Opened data successfully!')

# ---- PART 2: DISTINCT — Unique Values Only ----
# DISTINCT removes duplicate values — only one copy of each unique value is returned. 

# All unique genres in the Movie table
genres = pd.read_sql("""SELECT DISTINCT(Genre)
    FROM Movie;""", conn)
print(genres)

# All unique countries the actors come from
countries = pd.read_sql("""SELECT DISTINCT(Country)
    FROM Actor;""", conn)
print(countries)

# ---- PART 3: ORDER BY — Sorting Results ----
# ORDER BY sorts the result by a chosen column.
# Default order is ascending — smallest or earliest first.
# Add DESC to flip it — largest or latest first.

# All movies sorted by Rating — highest rated first
top_movies = pd.read_sql("""SELECT Title, Genre, Rating
    FROM Movie
    ORDER BY Rating DESC;""", conn)
print(top_movies)

# All movies sorted by Year — oldest first
oldest_first = pd.read_sql("""SELECT Title, Year
    FROM Movie
    ORDER BY Year;""", conn)
print(oldest_first)

# Actors sorted by Birth_Year — youngest first
youngest_actors = pd.read_sql("""SELECT Actor_Name, Birth_Year, Country
    FROM Actor
    ORDER BY Birth_Year DESC;""", conn)
print(youngest_actors)

# ---- PART 4: COUNT and SUM ----
# COUNT(column) returns the number of rows that match.
# SUM(column) returns the total of all values in a number column.
# Combine with WHERE to focus on specific rows.

# Total number of Action movies in the database
action_count = pd.read_sql("""SELECT COUNT(Movie_Id)
    FROM Movie
    WHERE Genre == 'Action';""", conn)
print(action_count)

# Total screen time (Duration) of all Animation movies
animation_mins = pd.read_sql("""SELECT SUM(Duration)
    FROM Movie
    WHERE Genre == 'Animation';""", conn)
print(animation_mins)

# ---- PART 5: AVG — Finding the Average ----
# AVG(column) calculates the mean of all values in a column.
# Use WHERE to average only rows that match a condition.

# Average rating of all movies in the database
avg_rating = pd.read_sql("""SELECT AVG(Rating)
    FROM Movie;""", conn)
print(avg_rating)

# Average duration of Action movies only
avg_action_dur = pd.read_sql("""SELECT AVG(Duration)
    FROM Movie
    WHERE Genre == 'Action';""", conn)
print(avg_action_dur)

# ---- PART 6: GROUP BY — Summarising by Category ----
# GROUP BY splits rows into groups by the values in one column.
# An aggregate function (COUNT, AVG, SUM) runs separately
# for each group — one result row per group.

# Count of movies in each genre
movies_per_genre = pd.read_sql("""SELECT Genre, COUNT(Movie_Id)
    FROM Movie
    GROUP BY Genre;""", conn)
print(movies_per_genre)

# Average rating per genre — sorted best genre first
avg_per_genre = pd.read_sql("""SELECT Genre, AVG(Rating)
    FROM Movie
    GROUP BY Genre
    ORDER BY AVG(Rating) DESC;""", conn)
print(avg_per_genre)

conn.close()
