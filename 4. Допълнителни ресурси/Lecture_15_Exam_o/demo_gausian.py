import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import statistics

# Plot between -10 and 10 with .001 steps.
# x_axis = np.arange(-20, 20, 0.01)
x_axis = np.arange(0, 24, 0.01)

# Calculating mean and standard deviation
# mean = statistics.mean(x_axis)
mean = 8
# sd = statistics.stdev(x_axis)
sd = 2
plt.plot(x_axis, norm.pdf(x_axis, mean, sd))
plt.show()
