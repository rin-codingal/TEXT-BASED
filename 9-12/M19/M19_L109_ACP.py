from pandas import read_csv
from collections import Counter
from matplotlib import pyplot
from sklearn.preprocessing import LabelEncoder

# Importing the dataset from the github
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/glass.csv"

# load the csv file as a data frame
df = read_csv(url, header=None)
data = df.values

# split into input and output elements
X, y = data[:, :-1], data[:, -1]

# label encode the target variable
y = LabelEncoder().fit_transform(y)

# summarize distribution
counter = Counter(y)
for k,v in counter.items():
	per = v / len(y) * 100
	print(f"Class={k}, n={v} ({round(per,3)}%)")

print()

#barplot
pyplot.bar(counter.keys(), counter.values())
pyplot.show()