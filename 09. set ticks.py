import numpy as np
import matplotlib.pyplot as plt

#data
sudut = np.arange(0,360,1)
y = np.sin(np.deg2rad(sudut))
plt.plot(sudut,y)
plt.xlabel("Sudut")
plt.ylabel("Amplitude")
# set ticks on X, Y

plt.xticks([0,90,180,270,360],[r'${0}^o$',r'${90}^o$',r'${180}^o$',r'${270}^o$',r'${360}^o$'])
plt.yticks([-1,0,1])
plt.show() 