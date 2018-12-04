import numpy as np
import matplotlib.pyplot as plt

def sinusGenerator(amplitude, frequency, time, theta):
    t = np.arange(0,time,0.1)
    y = amplitude * np.sin(2*frequency*t + np.deg2rad(theta))
    return t,y

t1, y1 = sinusGenerator(1,1,4,0)
plt.plot(t1,y1)
# add text inside graph/plot
# plt.text(Xpos,Ypos,"TEXT")
plt.text(2,1,"Sinus Wave")
plt.text(2,0.8,r"$\mathcal{Y} = A.sin(2 \omega t + \theta)$")
plt.xlabel("Time(second)")
plt.ylabel("Amplitude(cm)")
#show plot
plt.show()


