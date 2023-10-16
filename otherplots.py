mport matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(0.0, 1.0, 100000) # package numpy, subpackage random generates random data, function normal distribution/gaussian/bell curve
# center at 0.0, std dev/how spread out is the curve, 1000 points
plt.subplot(2, 1, 1) # 1 is number of columns in the subplot, 2 is number of rows in subplot, 1 is plot positioning
plt.hist(x, bins=80) # bar is bins, customize the number of bins

x = np.random.uniform(-4.0, 3.0, 100000) # lower bound is -4.0, upper bound is 3.0, generate 1000 data points
# uniform dist = equal likelihood of generating the lower and upper bound as any other number in it
plt.subplot(2, 1, 2) # 1 is number of columns in the subplot, 2 is number of rows in subplot, 2is plot positioning
plt.hist(x) # bar is bins, customize the number of bins
plt.show()