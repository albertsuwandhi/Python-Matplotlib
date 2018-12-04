import numpy as np
import matplotlib.pyplot as plt

'''
1. Prepare Data
2. Make Plot
3. Show Plot
'''
#1
x = np.array([1,3,5,7,9])
y1 = x**2
y2 = y1*2
#2 
plt.plot(x,y1)
plt.plot(x,y2)
#3
plt.show()