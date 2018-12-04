import numpy as np
import matplotlib.pyplot as plt

def sinusGenerator(amplitude, frequency, time, theta):
    t = np.arange(0,time,0.1)
    y = amplitude * np.sin(2*frequency*t + np.deg2rad(theta))
    return t,y

t1, y1 = sinusGenerator(1,1,5,0)
t2, y2 = sinusGenerator(1,1,5,45)
t3, y3 = sinusGenerator(1,1,5,60)
t4, y4 = sinusGenerator(1,1,5,90)

# Issue = no properties --> will be covered in next example
plt.plot(t1,y1,'r') # red
plt.plot(t2,y2,'b') # blue color solid
plt.plot(t3,y3,'b--') # blue --
#plt.plot(t4,y4,'y-*') # yellow -*
plt.plot(t4,y4,'yo') # yellow circle
plt.show()

'''
. point
, pixel
0 circle
color : 
r = red
b = blue
.
.
.
'''