import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt # for data visualization
import seaborn as sns # for statistical data visualization

import warnings
warnings.filterwarnings('ignore')

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

df = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M21\Live.csv")

print("shape:")
print(df.shape)
print()

#display the first 5 rows
print("The first 5 rows")
print(df.head())
print()

#info
print("Information")
df.info()
print()

print("total null data")
print(df.isnull().sum())
print()

# there are 4 redundant columns in the dataset. We should drop them before proceeding further.
df.drop(['Column1', 'Column2', 'Column3', 'Column4'], axis=1, inplace=True)

#info
print("Information after dropping some columns")
df.info()
print()

# redundant columns have been removed from the dataset
# there are 3 character variables (data type = object) and remaining 9 numerical variables (data type = int64)

#Descriptive statistics
print("Descriptive statistics")
print(df.describe())
print()

# view the labels in the variable
print(df['status_id'].unique())
print()

# view how many different types of variables are there
print("different types of variables based on status id:", len(df['status_id'].unique()))
print()

# view the labels in the variable
print(df['status_published'].unique())
print()

# view how many different types of variables are there
print("different types of variables based on status published:", len(df['status_published'].unique()))
print()

# view the labels in the variable
print(df['status_type'].unique())
print()

# view how many different types of variables are there
print("different types of variables based on status type:",len(df['status_type'].unique()))
print()

# Drop status_id and status_published variable from the dataset
df.drop(['status_id', 'status_published'], axis=1, inplace=True)

# View the summary of dataset again
print("summary dataset:")
print(df.info())
print()

#preview dataset again
#display the first 5 rows
print("The first 5 rows")
print(df.head())
print()

# Declare feature vector and target variable
X = df
y = df['status_type']

# Convert categorical variable into integers
le = LabelEncoder()

X['status_type'] = le.fit_transform(X['status_type'])

y = le.transform(y)

# View the summary of X
print("summary x:")
print(X.info())
print()

# Preview the dataset X
print("Preview the dataset X:")
print(X.head())
print()

# Feature Scaling
cols = X.columns

ms = MinMaxScaler()

X = ms.fit_transform(X)

X = pd.DataFrame(X, columns=[cols])

# Preview the dataset X
print("Preview the dataset X after feature scaling:")
print(X.head())
print()

# K-Means model with two clusters
kmeans = KMeans(n_clusters=2, random_state=0) 

print(kmeans.fit(X))
print()

# K-Means model parameters study
print(kmeans.cluster_centers_)
print()

# Check quality of weak classification by the model
labels = kmeans.labels_

# check how many of the samples were correctly labeled
correct_labels = sum(y == labels)

print("Result: %d out of %d samples were correctly labeled." % (correct_labels, y.size))
print()

print('Accuracy score: {0:0.2f}'. format(correct_labels/float(y.size)))
print()

# Use elbow method to find optimal number of clusters
cs = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
    kmeans.fit(X)
    cs.append(kmeans.inertia_)
plt.plot(range(1, 11), cs)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('CS')
plt.show()

kmeans = KMeans(n_clusters=2,random_state=0) #with 2 clusters

kmeans.fit(X)

labels = kmeans.labels_

# check how many of the samples were correctly labeled

correct_labels = sum(y == labels)

print("Result: %d out of %d samples were correctly labeled." % (correct_labels, y.size))

print('Accuracy score: {0:0.2f}'. format(correct_labels/float(y.size)))
print()

