# https://matplotlib.org/stable/gallery/statistics/hist.html

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(0.0, 1.0, 100000) # package numpy, subpackage random generates random data, function normal distribution/gaussian/bell curve
# center at 0.0, std dev/how spread out is the curve, 1000 points

plt.hist(x, bins=80) # bar is bins, customize the number of bins

plt.show()