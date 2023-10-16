# https://matplotlib.org/stable/tutorials/pyplot.html#sphx-glr-tutorials-pyplot-py

import matplotlib.pyplot as plt

'''
plt.plot([1, 2, 3, 4], [1, 4, 9, 16]) # will create crooked line instead of what it should be - a curve
plt.ylabel('some numbers')
plt.show()
'''
plt.plot([1, 2, 3, 4], [1, 4, 9, 16],'g^')  # plot x and y using blue circle markers
plt.ylabel('some numbers')
plt.show()
