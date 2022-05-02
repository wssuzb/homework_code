import numpy as np
import random

def mcmc(N, x_range):
    sum = 0
    for i in range(N):
        x = random.uniform(0, int(x_range))
        sum += np.exp(-x**2/2)

    return 1/N * (1/np.sqrt(2*np.pi)) * sum

print(mcmc(10000, x_range = 1))
print(mcmc(10000, x_range = 5))