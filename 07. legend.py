import numpy as np
import matplotlib.pyplot as plt

def sinusGenerator(amplitude, frequency, time, theta):
    t = np.arange(0,time,0.1)
    y = amplitude * np.sin(2*frequency*t + np.deg2rad(theta))
    return t,y

t1, y1 = sinusGenerator(1,1,4,0)
t2, y2 = sinusGenerator(1,1,4,90)

# 1st Type
# plt.plot(t1,y1, label="sin(0)")
# plt.plot(t2,y2, label="sin(90)")
# plt.legend()

# 2nd Type
# plt.plot(t1,y1, label="sin(0)")
# plt.plot(t2,y2, label="sin(90)")
# plt.legend(loc="upper center")

# 3rd Type
# plt.plot(t1,y1, label="sin(0)")
# plt.plot(t2,y2, label="sin(90)")
# plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05))

# 4th Type
plt.figure(1)
ax = plt.subplot(111)
plt.plot(t1,y1, "r--", label="sin(0)" )
plt.plot(t2,y2, "b--", label="sin(90)")
box = ax.get_position()
# shrink to 0.75
ax.set_position([box.x0, box.y0, box.width*0.75, box.height])
plt.legend(loc="upper center", bbox_to_anchor=(1.2,1))
plt.xlabel("Time(second)")
plt.ylabel("Amplitude(cm)")

#show plot
plt.show()


