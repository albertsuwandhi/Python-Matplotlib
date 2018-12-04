import numpy as np
import matplotlib.pyplot as plt

def sinusGenerator(amplitude, frequency, time, theta):
    t = np.arange(0,time,0.1)
    y = amplitude * np.sin(2*frequency*t + np.deg2rad(theta))
    return t,y

t1, y1 = sinusGenerator(1,1,4,0)
t2, y2 = sinusGenerator(1,1,4,90)
t3, y3 = sinusGenerator(1,1,4,180)

sinPlot1 = plt.plot(t1,y1)
sinPlot2 = plt.plot(t2,y2)
sinPlot3 = plt.plot(t3,y3)

plt.setp(sinPlot1,color='r',linestyle = '-', linewidth =0.75)
plt.setp(sinPlot2,color='g',linestyle = '--', linewidth =1.5)
plt.setp(sinPlot3,color='b',linewidth = 2)
plt.show()
