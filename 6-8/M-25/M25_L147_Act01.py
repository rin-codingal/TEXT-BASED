import pandas as pd
import matplotlib.pyplot as plt

countries_df = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\6-8\M-25\Countries Data.csv")

#copy the dataframe
countries = countries_df

print("first 3 rows of countries:")
print(countries.head(3))
print()

#Extract the rows where the year is 1952
print("first 3 rows of countries in year 1952:")
c_52 = countries.loc[countries['year'] == 1952]
print(c_52.head())
print()

# Extract the rows where the year is 2007
print("first 3 rows of countries in year 2007:")
c_07 = countries.loc[countries['year'] == 2007]
print(c_07.head())
print()

print(type(c_52))

print()

# Merge the '52 and the '07 dataframes together
print("first 5 rows of merge data for year 1952 and 2007:")
c_merge = c_52.merge(c_07, left_on='country', right_on='country')
print(c_merge.head())
print()

#Drop both the year columns
print("after dropping column year:")
c_merge.drop(['year_x', 'year_y'], axis=1)
print(c_merge.head())
print()

# Create a new column that takes the difference between the population_y and the population_x column
print("after creating new column 'population growth'")
c_merge['population_growth'] = c_merge['population_y'] - c_merge['population_x']
print(c_merge.head())
print()

print(c_merge.shape)

print(type(c_merge))
print()

# Sort the values so you get back the 10 countries with the biggest population growth
print("biggest population growth after sort the values:")
c_merge = c_merge.sort_values('population_growth', ascending=False).head(10)
print(c_merge.head(10))
print()
      
# Reset the Index
print("after resetting index:")
c_merge = c_merge.reset_index()
print(c_merge.head(10))
print()

print(c_merge.shape)
print()

# Drop the index column
print("after drop index column: ")
c_merge = c_merge.drop(['index'], axis=1)
print(c_merge.shape)
print()

# We have our top ten countries with the highest population from the years between 1952 and 2007!
print(c_merge)

# plot our data
names = ['China', 'India', 'United States', 'Indonesia', 'Brazil', 'Pakistan', 'Bangledesh', 'Nigeria', 'Mexico', 'Philippines']
pop_grow = (c_merge['population_growth'] / 10**6)

plt.figure(figsize=(15,9))
plt.bar(names,pop_grow,width=0.6)
plt.xlabel('Country')
plt.ylabel('Population Growth (Millions)')
plt.title('Top 10 Countries w/the Biggest Population Growth from 1952 to 2007')
plt.xticks(rotation=45)

# zip joins x and y coordinates in pairs
for x,y in zip(names,pop_grow):

    label = "{:.2f}".format(y)

    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.show()