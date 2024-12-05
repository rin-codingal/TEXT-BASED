import pandas as pd

#rating
rating_df = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M19\ratings.csv")

#display the first 5 rows of rating
print("First 5 rows of ratings data:")
print(rating_df.head())
print()

#movie
movie_df = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M19\movies.csv")

#display the first 5 rows of movies
print("First 5 rows of movies data:")
print(movie_df.head())
print()

# extract year from title and assign it to a new column
movie_df["year"] = movie_df.title.str.extract("(\(\d\d\d\d\))", expand = True)
print("updated first 5 rows of movie data with 'year' column:")
print(movie_df.head())
print()

#Remove parantheses from year
movie_df["year"] = movie_df.year.str.extract("(\d\d\d\d)", expand=True)
print("updated first 5 rows of movie data with 'year' column parentheses removed:")
print(movie_df.head())
print()

#Remove year from title
movie_df["title"] = movie_df.title.str.replace("(\(\d\d\d\d\))","tes")
print("updated first 5 rows of movie data:")
print(movie_df.head())
print()

#Remove all the whitespaces from title
movie_df["title"] = movie_df["title"].apply(lambda x: x.strip())

#Convert Genres into a list
movie_df["genres"] = movie_df.genres.str.split("|")
print("updated first 5 rows of movie data with genre as list:")
print(movie_df.head())
print()

#encoding of genre
movies_copy = movie_df.copy()

for index, row in movie_df.iterrows():
  for genre in row["genres"]:
    movies_copy.at[index, genre] = 1

print("first 5 rows of data with encoded genres:")
print(movies_copy.head())
print()

#Filling NAN values with 0
movies_copy = movies_copy.fillna(0)
print("first 5 rows of data after filling up NaN value:")
print(movies_copy.head())
print()

#display the first 5 rows of rating
print("First 5 rows of ratings data:")
print(rating_df.head())
print()

# drop timestamp column
rating_df = rating_df.drop(["timestamp"], axis=1)
print("First 5 rows of ratings data after dropping 'timestamp' column:")
print(rating_df.head())
print()

# taking User Input for ratings of different movies
user_input = [
              {'title' : 'Grand Slam', 'rating' : 5.6},
              {'title' : 'Zero', 'rating' : 7},
              {'title' : 'Jumanji', 'rating' : 8.5},
              {'title' : 'Toy Story', 'rating' : 4.5}
]

movies_input = pd.DataFrame(user_input)
print("movies input from user:")
print(movies_input)
print()

#Add movieID to user input
#First we will filter selected movies from original dataset
input_id = movie_df[movie_df["title"].isin(movies_input["title"].tolist())]

#Merging the two datasets
movies_input = pd.merge(input_id, movies_input)
print("movies input from user after meging 2 datasets:")
print(movies_input)
print()

#check for same movies given in input in original dataset
movies_user = movies_copy[movies_copy["movieId"].isin(movies_input["movieId"].tolist())]
print("check same movies between user input and original dataset:")
print(movies_user)
print()

#reset index
movies_user = movies_user.reset_index(drop=True)
print("check same movies between user input and original dataset after resetting index:")
print(movies_user)
print()

# create genre table
UserGenreTable = movies_user.drop(["movieId", "title", "genres", "year"], axis=1)
print("user genre table:")
print(UserGenreTable)
print()

#dot product to get weights
UserProfile = UserGenreTable.transpose().dot(movies_input['rating'])

#User Profile for every genre
print("user profile for every genre:")
print(UserProfile)
print()

#Create a genre table for every movie in original datset
GenreTable = movies_copy.set_index(movies_copy['movieId'])
print("Genre table:")
print(GenreTable)
print()

#drop some column
GenreTable = GenreTable.drop(['movieId','title','genres','year'], axis=1)
print("updated the first 5 rows of genre table:")
print(GenreTable.head())
print()

#Final Recommendation value for each movie
Recommendation_df = ((GenreTable*UserProfile).sum(axis=1))/UserProfile.sum()
print("recommendation value:")
print(Recommendation_df.head())
print()

#Sort the values to get movies with high recommendation values
Recommendation_df = Recommendation_df.sort_values(ascending=False)
print("first 5 rows of recommendation after sorting:")
print(Recommendation_df.head())
print()

#Final recommendation table for movies
RecommendationTable =  movie_df.loc[movie_df['movieId'].isin(Recommendation_df.head(20).keys())]
print("final recommendation table:")
print(RecommendationTable)
print()

