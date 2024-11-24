import numpy as np

np.random.seed(42)

# 1 represents the puppies with blue eyes, and 0 represents the puppies with hazel eyes.
puppies = np.array([1,0,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1])

#Finding the proportion of puppies with blue eyes in the above array. 
#Storing this value in a variable p
p=puppies.mean()

print(f"Mean: {p}")
print(f"Standard Deviation: {puppies.std()}")
print(f"Variance: {puppies.var()}")
print()
print()

#Using numpy's random.choice to simulate 5 draws from the puppies array.
np.random.choice(puppies, size=(1,5), replace=True)
np.random.choice(puppies, size=(1,5), replace=True).mean()

#Proportion of sample with blue eyes in 0.8

#Repeating the above to obtain 10,000 additional proportions, where 
#each sample was of size 5. Storing these in a variable called sample_props
print("Sampling Distribution with size 5:")

sample_props= []

for i in range(10000):
    sample = np.random.choice(puppies, 5, replace=True)
    sample_props.append(sample.mean())

sample_props = np.array(sample_props)

#The mean of the sampling distribution
sm = sample_props.mean()
print(f"Mean: {sample_props.mean()}")
print(f"Standard Deviation: {sample_props.std()}")
print(f"Variance: {sample_props.var()}")
print()

print("Sampling Distribution with size 20:")

twenty_sample_props= []

for i in range(10000):
    sample = np.random.choice(puppies, 20, replace=True)
    twenty_sample_props.append(sample.mean())
twenty_sample_props = np.array(twenty_sample_props)

print(f"New Mean: {twenty_sample_props.mean()}")
print(f"New Standard Deviation: {twenty_sample_props.std()}")
print(f"New Variance: {twenty_sample_props.var()}")
