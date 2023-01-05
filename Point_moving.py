
%matplotlib notebook
from ipywidgets import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor
from matplotlib.widgets import Slider, Button

#x and y arrays for definining an initial function
x_points = [1,2,3,4,5,6,7]
y_points = [2,1,3,45,56,78,90]

# Plotting
fig = plt.figure()
#ax = fig.subplots()
ax=plt.axes([0, 0, 0.5, 0.5])
ax2 = plt.axes([0, 0.5, 0.5, 0.5])

ax.scatter(x_points,y_points, color = 'b')
ax.grid()

# Defining the cursor
cursor = Cursor(ax, horizOn=True, vertOn=True, useblit=True,
                color = 'r', linewidth = 1)

# Creating an annotating box
annot = ax.annotate("", xy=(0,0), xytext=(-40,40),textcoords="offset points",
                    bbox =dict(boxstyle='round4', fc='linen',ec='k',lw=1),
                    arrowprops=dict(arrowstyle='-|>'))
annot.set_visible(False)

# Function for storing and showing the clicked values
coord = []
list=[]
def onclick(event):
    global coord
    coord.append((event.xdata, event.ydata))
    x = event.xdata
    y = event.ydata

    
    # printing the values of the selected point
    print([x,y])
    list.append(x)
    annot.xy = (x,y)
    text = "({:.2g}, {:.2g})".format(x,y)
    annot.set_text(text)
    annot.set_visible(True)
    fig.canvas.draw() #redraw the figure


def slide(event):
        freq = Slider(ax2,'Frequency', 0.0, 2, 3)
        fig.canvas.draw() #redraw the figure

    
    
    
fig.canvas.mpl_connect('button_press_event', onclick)
fig.canvas.mpl_connect('button_press_event', slide)

plt.show()



    
