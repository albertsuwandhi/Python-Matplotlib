import numpy as np
import matplotlib.pyplot as plt

#data
sudut = np.arange(0,360,1)
y = np.sin(np.deg2rad(sudut))
plt.plot(sudut,y,'r--')
plt.title("Sinus Wave")
plt.text(180,1,"Amplitude")
plt.text(360, 0.1, "Sudut")
# set ticks on X, Y
plt.xticks([0,90,180,270,360],[r'${0}^o$',r'${90}^o$',r'${180}^o$',r'${270}^o$',r'${360}^o$'])
plt.yticks([-1,0,1])
#gca = get current axis
ax = plt.gca()
#ax.spines['left'].set_position(('axes',0.5)) # 0.5 dari 360 => center (180)
ax.spines['left'].set_position(('data',180))
ax.spines['left'].set_color('blue')
ax.spines['bottom'].set_position(('data',0))
ax.spines['bottom'].set_color('blue')
ax.spines['right'].set_color('none') #remove spines
ax.spines['top'].set_color('none') #remove spines
plt.show() 