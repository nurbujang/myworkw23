import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1.0, 20.0, 0.1) # 1 to 10 in increments of 0.1

plt.plot(x, x**2, 'g-', label='x^2')
plt.plot(x, x**3, 'b-', label='x^3') # multiply by itself 3 times
plt.plot(x, x**4, 'r-', label='x^4') # multiply by itself 4 times
plt.plot(x, 2**x, 'k-', label='2^x')

plt.legend()

plt.show()