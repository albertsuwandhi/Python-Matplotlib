import numpy as np
import matplotlib.pyplot as plt
# line
x = np.arange(1,11,1)
print (x)
y = 2*x + 3
print(y)
#split plot - 1
plt.figure(1)
plt.plot(x,y)
#plt.show()
# circle
radius = 5
#sudut = np.arange(0,2*np.pi,0.1)
sudut = np.linspace(0,2*np.pi,100)
x1 = radius*np.cos(sudut)
y1 = radius*np.sin(sudut)
#split plot - 2
plt.figure(2)
plt.plot(x1,y1)
plt.show()