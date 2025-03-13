import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer

dataset = load_breast_cancer()

sns.set_style("dark")
import matplotlib as mpl
mpl.style.use(["https://gist.githubusercontent.com/BrendanMartin/01e71bb9550774e2ccff3af7574c0020/raw/6fa9681c7d0232d34c9271de9be150e584e606fe/lds_default.mplstyle"])
mpl.rcParams.update({"figure.figsize": (8,6), "axes.titlepad": 22.0})

print(f"Target variables  : {dataset['target_names']}")
print()

(unique, counts) = np.unique(dataset["target"], return_counts=True)

print(f"Unique values of the target variable: {unique}")
print()

print(f"Counts of the target variable : {counts}")
print()

#barplot
sns.barplot(x=dataset['target_names'], y=counts, hue=dataset['target_names'])
plt.title("Target variable counts in dataset")
plt.show()