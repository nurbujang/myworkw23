# can plot functions too
# https://matplotlib.org/stable/gallery/shapes_and_collections/scatter.html

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2.0 * np.pi, 2.0 * np.pi, 0.1) # pi is just a number 3.142, 0.1 is interval
# a number going from -6++ in intervals of 0.1

plt.plot(x, np.sin(x), 'g.') # from -6+ to +ve 6++
plt.plot(x, np.cos(x), 'b.')

plt.show()