import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix, classification_report

# Load the dataset
df = pd.read_csv(r"C:\Users\nurin\Documents\CODINGAL\CLASS\PAID\TEXT-BASED\9-12\M21\College.csv")

# Set the visualization style
sns.set_theme(style="whitegrid")

# =====================================================================
# 1. Scatterplot: Grad. Rate vs Room.Board colored by Private
# =====================================================================
sns.scatterplot(data=df, x='Room.Board', y='Grad.Rate', hue='Private', alpha=0.7)
plt.title('Graduation Rate vs. Room & Board Costs')
plt.xlabel('Room & Board ($)')
plt.ylabel('Graduation Rate (%)')
plt.tight_layout()
plt.show()
plt.clf()  # Clear figure for the next plot

# =====================================================================
# 2. Scatterplot: F.Undergrad vs Outstate colored by Private
# =====================================================================
sns.scatterplot(data=df, x='Outstate', y='F.Undergrad', hue='Private', alpha=0.7)
plt.title('Full-time Undergraduates vs. Out-of-State Tuition')
plt.xlabel('Out-of-State Tuition ($)')
plt.ylabel('Full-time Undergraduates')
plt.tight_layout()
plt.show()
plt.clf()

# =====================================================================
# 3. Histogram for the Grad. Rate column
# =====================================================================
sns.histplot(data=df, x='Grad.Rate', hue='Private', bins=20, multiple='stack', alpha=0.7)
plt.title('Histogram of Graduation Rates by School Type')
plt.xlabel('Graduation Rate (%)')
plt.ylabel('Count')
plt.tight_layout()
plt.show()
#plt.savefig('histogram_grad_rate.png')
plt.clf()

# =====================================================================
# 4. K-Means Cluster Creation
# =====================================================================
# Drop identifier columns and the 'Private' target text labels for unsupervised learning
X = df.drop(columns=['Unnamed: 0', 'Private'])

# Create and fit the KMeans model with 2 clusters
kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(X)
cluster_labels = kmeans.labels_

# =====================================================================
# 5. Confusion Matrix and Classification Report
# =====================================================================
# Convert the 'Private' column to binary numbers ('Yes' -> 1, 'No' -> 0)
true_labels = df['Private'].map({'Yes': 1, 'No': 0}).values

# Unsupervised clusters labels (0 and 1) are randomly assigned.
# If the initial alignment yields lower than 50% accuracy, we flip the labels to match the ground truth orientation.
cm_initial = confusion_matrix(true_labels, cluster_labels)
if np.diag(cm_initial).sum() / cm_initial.sum() < 0.5:
    cluster_labels = 1 - cluster_labels

# Compute final metrics
cm = confusion_matrix(true_labels, cluster_labels)
report = classification_report(true_labels, cluster_labels, target_names=['Public (No)', 'Private (Yes)'])

print("Confusion Matrix:")
print(cm)
print("\nClassification Report:")
print(report)