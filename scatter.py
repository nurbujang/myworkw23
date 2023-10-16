# https://matplotlib.org/stable/tutorials/pyplot.html
# https://matplotlib.org/stable/gallery/shapes_and_collections/scatter.html

import matplotlib.pyplot as plt
import numpy as np

x1 = np.random.uniform(0.0, 10.0, 100) # lower bound is -0.0, upper bound is 10.0, generate 100 data points
# uniform dist = equal likelihood of generating the lower and upper bound as any other number in it
x2 = np.random.uniform(0.0, 5.0, 100)
x3 = np.random.randint(0, 20, 100) # random integer
x4 = np.random.normal(0.0, 10.0, 100) # package numpy, subpackage random generates random data, function normal distribution/gaussian/bell curve
# center at 0.0, std dev/how spread out is the curve, 1000 points

plt.scatter(x1, x2, c=x3, s=x4) # x dimension, y dimension, colored dot in 3rd dimension, sized dot in 4th dimension
# color has to be integer bc doesnt work so well in floats
plt.show()