import matplotlib.pyplot as plt

import random

x = [random.normalvariate(0,1) for _ in range(1000)]

plt.figure(figsize=(5,3))
plt.hist(x, bins=20, alpha=0.5)
plt.ylabel('frequency')
plt.show()
