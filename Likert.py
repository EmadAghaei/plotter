import matplotlib.pylab as plt
import numpy as np
import pandas as pd

df4 = pd.DataFrame.from_dict({'bikes1':[-1,-2,-3,-4,-5,-3], 'bikes':[10,20,30,15,11,11],
 'cats':[1,2,3,4,5,6], 'cats1':[-6,-5,-4,-3,-2,-1], 'Year': [2012,2013,2014,2015,2016,2017]})


#Create the general blog and the "subplots" i.e. the bars
f, ax1 = plt.subplots(1, figsize=(10,5))
# Set the bar width
bar_width = 0.8
# positions of the left bar-boundaries
bar_l = [i+1 for i in range(len(df4['bikes']))]
# positions of the x-axis ticks (center of the bars as bar labels)
tick_pos = [i+(bar_width/2) for i in bar_l]

# Create a bar plot, in position bar_1
ax1.barh(bar_l, df4['bikes1'],  label='bikes1', alpha=0.5,color='r', align='center')
# Create a bar plot, in position bar_1
ax1.barh(bar_l, df4['bikes'],alpha=0.5,color='b',left='bikes1', label='bikes', align='center')
# Create a bar plot, in position bar_1
# ax1.barh(bar_l, df4['cats1'], label='cats1', alpha=0.5,color='y', align='center',
#  left=[min(i,j) for i,j in zip(df4['bikes'],df4['bikes1'])])
# # Create a bar plot, in position bar_1
# ax1.barh(bar_l, df4['cats'], alpha=0.5,color='g', label='cats', align='center',
#  left=[max(i,j) for i,j in zip(df4['bikes'],df4['bikes1'])])


# set the x ticks with names
plt.xticks(tick_pos, df4['Year'])
# Set the label and legends
ax1.set_ylabel("Count")
ax1.set_xlabel("Year")
plt.legend(loc='upper left')
ax1.axhline(y=0, color='k')
ax1.axvline(x=0, color='k')

# Set a buffer around the edge
plt.xlim([min(tick_pos)-bar_width, max(tick_pos)+bar_width])
plt.show()