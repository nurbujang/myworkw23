# https://matplotlib.org/stable/tutorials/pyplot.html#sphx-glr-tutorials-pyplot-py

import matplotlib.pyplot as plt
import numpy as np

# create variable called x
x = np.arange (0.0, 10.0, 0.01  ) # 0.0 lower bound, 10 (to upper bound but not including upper bound)                                                                                
# last argument is increment
# in numpy package, theres a function called arange 
# arange (similar to range, but range only works with integer values, NO FLOATING POINTS OR DECIMAL VALUES)
y = 3.0*x
noise = np.random.normal(0.0, 1.0, len(x)) # variable 3 (noise) in normal distribution
# distribution will be centered at 0.0, std dev 1.0 (if 2, bigger), len(x) is how many values we want, same length of x

plt.plot(x,y,'g^')  # plot x and y using green triangle markers
# plt.plot(x,noise,'b-') # blue dash
plt.plot(x, y + noise,'b-') # noisy line
plt.ylabel('some numbers')                  
plt.show()