import numpy as np
import matplotlib.pyplot as plt

def sinusGenerator(amplitude, frequency, time, theta):
    t = np.arange(0,time,0.1)
    y = amplitude * np.sin(2*frequency*t + np.deg2rad(theta))
    return t,y

amplitude = 1
frequency = 1
time = 4
theta = 90
t1, y1 = sinusGenerator(amplitude,frequency,time,theta)
plt.plot(t1,y1,"r--")
# use r"$ $" = raw string, for more formatting see regex
title1 = "Sinus Wave\n"
title2 =r"$\mathcal{Y} = A.sin(2 \omega t + \theta)$" + "\n" 
title3 = r"$ \omega = $" + str(frequency) + r"$\mathit{Hz}$" + " "
title4 = r"$ \theta = $" + str(theta) + r"$^{o}$" + "Amplitude = " + str(amplitude)
plt.title(title1 + title2 + title3 + title4)
plt.xlabel("Time(second)")
plt.ylabel("Amplitude(cm)")
# plt.axis([xmin,xmax, ymin,ymax])
#plt.axis([0,4,-1,1])
plt.show()
