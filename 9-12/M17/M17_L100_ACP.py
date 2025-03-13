import scipy.stats as stats

# calculate probability
prob = stats.binom.pmf(2, n=10, p=.5) + stats.binom.pmf(3, n=10, p=.5) + stats.binom.pmf(4, n=10, p=.5)

print(f"Probability of observing between 2 and 4 heads: {prob}")
print()