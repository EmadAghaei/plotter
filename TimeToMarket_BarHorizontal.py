# libraries
import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap

# Make fake dataset
controlData = [4, 12, 3, 2, 2, 4, 10, 3, 5, 1, 2, 7, 10, 10]
experimentalData = [28, 31]
controlSessions = ("Session14 (C)", "Session13 (C)", "Session12 (C)",
         "Session11 (C)", "Session10 (C)", "Session9 (C)", "Session8 (C)", "Session7 (C)", "Session6 (C)",
         "Session5 (C)","Session4 (C)", "Session3 (C)", "Session2 (C)","Session1 (C)")
experimentalSession = ("Session2 (E)", "Session1 (E)")



# Create horizontal bars
plt.barh(["Mean of session1-2 (E)"],[29.5],color="#58508d")
plt.barh(["Mean of session1-14 (C)"],[5.4], color="#ff6361")
plt.barh([" "],[0])

plt.barh([" "],[0])
p2= plt.barh(experimentalSession,experimentalData,color="#58508d" )
p1= plt.barh(controlSessions, controlData, color="#ff6361")
# Create names on the y-axis

# plt.yticks(y_pos2, bars2)
# plt.yticks(y_pos, bars)


plt.xticks(np.arange(0, 40, 3))
plt.title('Time-to-market of control(C) and experimental(E) sessions')
plt.xlabel('Number of correctly implemented behaviors')
plt.ylabel('Sessions')

#legend
labels=['Correctly implemented behaviors at the end of controlled sessions by one developer.',
        'Correctly implemented behaviors at the end of experimental condition by 7 developers.']
labels = [ '\n'.join(wrap(l, 30)) for l in labels]
plt.legend(labels)

plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)

plt.subplots_adjust(left=0.29, right=0.90, top=0.95, bottom=0.1)
# Show graphic
# plt.show();
plt.savefig("./data/timeToMarket.pdf");








