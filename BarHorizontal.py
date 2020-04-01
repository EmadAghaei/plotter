# libraries
import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap

# Make fake dataset
height = [0,0,5.4,0,4,12,3,2,2,4,10,3,5,1,2,7,10,10]
height2 = [31,28]
bars = ( "Session2 (E)", "Session1 (E)", "Mean Sessions1-14 (C)","", "Session14 (C)", "Session13 (C)", "Session12 (C)",
         "Session11 (C)", "Session10 (C)", "Session9 (C)", "Session8 (C)", "Session7 (C)", "Session6 (C)",
         "Session5 (C)","Session4 (C)", "Session3 (C)", "Session2 (C)","Session1 (C)" )
bars2 = ("E Session1", "E Session2")
y_pos = np.arange(len(bars))
y_pos2 = np.arange(len(bars2))


# Create horizontal bars
p1= plt.barh(y_pos, height,color="#ff6361" )
p2= plt.barh(y_pos2, height2,color="#58508d" )

# Create names on the y-axis

# plt.yticks(y_pos2, bars2)
plt.yticks(y_pos, bars)


plt.xticks(np.arange(0, 40, 3))
plt.title('Time-to-market of controlled(C) and experimental(E) sessions')
plt.xlabel('Number of correctly implemented behaviors')
plt.ylabel('Sessions')

#legend
labels=['Correctly implemented behaviors at the end of controlled sessions by one developer.','Correctly implemented behaviors at the end of experimental condition by 7 developers.']
labels = [ '\n'.join(wrap(l, 37)) for l in labels]
plt.legend(labels)

plt.subplots_adjust(left=0.27, right=0.96, top=0.95, bottom=0.1)
# Show graphic
# plt.show();
plt.savefig("./data/timeToMarket.pdf");








