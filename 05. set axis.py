import numpy as np
import matplotlib.pyplot as plt

def sinusGenerator(amplitude, frequency, time, theta):
    t = np.arange(0,time,0.1)
    y = amplitude * np.sin(2*frequency*t + np.deg2rad(theta))
    return t,y

t1, y1 = sinusGenerator(1,1,4,0)
t2, y2 = sinusGenerator(1,1,4,90)


plt.plot(t1,y1)
plt.plot(t2,y2)
# plt.axis([xmin,xmax, ymin,ymax])
plt.axis([0,4,-1,1])
plt.show()
