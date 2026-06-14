import pandas as pd
import matplotlib.pyplot as plt

countries_df = pd.read_csv(r"")

#copy the dataframe


print("first 3 rows of countries:")

print()

#Extract the rows where the year is 1952
print("first 3 rows of countries in year 1952:")


print()

# Extract the rows where the year is 2007
print("first 3 rows of countries in year 2007:")


print()



print()

# Merge the '52 and the '07 dataframes together
print("first 5 rows of merge data for year 1952 and 2007:")


print()

#Drop both the year columns
print("after dropping column year:")


print()

# Create a new column that takes the difference between the population_y and the population_x column
print("after creating new column 'population growth'")


print()




print()

# Sort the values so you get back the 10 countries with the biggest population growth
print("biggest population growth after sort the values:")


print()
      
# Reset the Index
print("after resetting index:")


print()


print()

# Drop the index column
print("after drop index column: ")


print()

# We have our top ten countries with the highest population from the years between 1952 and 2007!


# plot our data
names = ['China', 'India', 'United States', 'Indonesia', 'Brazil', 'Pakistan', 'Bangledesh', 'Nigeria', 'Mexico', 'Philippines']


plt.figure(figsize=(15,9))
plt.bar()
plt.xlabel('Country')
plt.ylabel('Population Growth (Millions)')
plt.title('Top 10 Countries w/the Biggest Population Growth from 1952 to 2007')
plt.xticks(rotation=45)

# zip joins x and y coordinates in pairs
for x,y in zip(,):

    label = "{:.2f}".format(y)

    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.show()