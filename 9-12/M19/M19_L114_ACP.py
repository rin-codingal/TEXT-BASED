import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Get the data
column_names = ["user_id", "item_id", "rating", "timestamp"]

path = "https://media.geeksforgeeks.org/wp-content/uploads/file.tsv"

df = pd.read_csv(path, sep="\t", names=column_names)

#display the first 5 rows of data
print("First 5 rows of data:")
print(df.head())
print()

# Check out all the movies and their respective IDs
movie_titles = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/Movie_Id_Titles.csv")

#display the first 5 rows of data
print("First 5 rows of movie titles data:")
print(movie_titles.head())
print()

#merge data
data = pd.merge(df, movie_titles, on="item_id")

#display the first 5 rows of data
print("First 5 rows of merged data:")
print(data.head())
print()

# Calculate mean rating of all movies
mean_rate = data.groupby("title")["rating"].mean().sort_values(ascending=False)
print("First 5 rows of mean rating data:")
print(mean_rate.head())
print()

# calculate count rating
count_rate = data.groupby("title")["rating"].count().sort_values(ascending=False)
print("First 5 rows of count rating data:")
print(count_rate.head())
print()

# creating dataframe with rating count values
ratings = pd.DataFrame(data.groupby("title")["rating"].mean())

ratings["num of ratings"] = pd.DataFrame(data.groupby("title")["rating"].count())
print("First 5 rows of rating count value:")
print(ratings.head())
print()

sns.set_style("white")

# histplot of 'num of ratings column'
plt.figure(figsize =(10, 4))

ratings["num of ratings"].hist(bins = 70)
plt.show()

# histplot of 'ratings' column
plt.figure(figsize =(10, 4))

ratings["rating"].hist(bins = 70)
plt.show()


moviemat = data.pivot_table(index ="user_id",
			columns ="title", values ="rating")

print("pivot table of movie:")
print(moviemat.head())
print()

# Sorting values according to the 'num of rating column'
sort_rating = ratings.sort_values("num of ratings", ascending = False)
print("sorting rating:")
print(sort_rating.head(10))
print()

# analysing correlation with similar movies
starwars_user_ratings = moviemat['Star Wars (1977)']
liarliar_user_ratings = moviemat['Liar Liar (1997)']

print("the first 5 rows of starwars user ratings:")
print(starwars_user_ratings.head())
print()

# analysing correlation with similar movies
similar_to_starwars = moviemat.corrwith(starwars_user_ratings)
similar_to_liarliar = moviemat.corrwith(liarliar_user_ratings)

corr_starwars = pd.DataFrame(similar_to_starwars, columns =["Correlation"])
corr_starwars.dropna(inplace = True)

print("the first 5 rows of correlation Starwars:")
print(corr_starwars.head())
print()

# Similar movies like starwars
sort_corr_starwars = corr_starwars.sort_values('Correlation', ascending = False)
print("first 10 rows of sorted correlation starwars:")
print(sort_corr_starwars.head(10))
print()

corr_starwars = corr_starwars.join(ratings['num of ratings'])
print("first 5 rows of correlation starwars join with ratings:")
print(corr_starwars.head())
print()

sort_join = corr_starwars[corr_starwars['num of ratings']>100].sort_values('Correlation', ascending = False)
print("first 5 rows of sorted correlation starwars joined with ratings")
print(sort_join.head())
print()

# Similar movies as of liarliar
corr_liarliar = pd.DataFrame(similar_to_liarliar, columns =['Correlation'])
corr_liarliar.dropna(inplace = True)

corr_liarliar = corr_liarliar.join(ratings['num of ratings'])
sort_liar = corr_liarliar[corr_liarliar['num of ratings']>100].sort_values('Correlation', ascending = False)
print("first 5 rows of correlation liarliar after sorting:")
print(sort_liar.head())
print()

