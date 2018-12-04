import matplotlib.pyplot as plt 

activities = ["sleep", "eat", "play", "sport", "work"]
hours = [7,2,5,3,8]
#define color in pie chart
'''
Colors can be added to graph by one of the following ways:

    Hex value (#_ _ _ _ _ _)
    rgb value ( r , g , b ) or ( r , g , b , a ) where r, g, b, a are in range 0–1
    grey shades (0–1 range)
    as in active color cycle ( “c0”, “c1”)[capital C followed by digit]
'''
#colors = ['b','r']
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#00cc99']
#only explode the "work" portion
explode = (0, 0, 0, 0, 0.1) 
#autopct = percentage 1 decimal only
plt.pie(hours,labels=activities,explode=explode, shadow = True, startangle=90, colors=colors, autopct='%.1f%%')
plt.title('My Activities')
#draw center circle
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
#show plot
plt.show()