import matplotlib.pyplot as plt
import numpy as np
from textwrap import wrap
import matplotlib as mpl


participants = ["M14", "M13", "M12", "M11", "M10", "M9", "M8", "M7", "M6", "M5", "M4", "M3", "M2", "M1","", "C14", "C13", "C12", "C11", "C10", "C9", "C8", "C7", "C6", "C5", "C4", "C3", "C2", "C1", " "
  ," "  , "Mean M1-14", "Mean C1-14"]
# addedd zero as seperator
training_task=[30,10,17,15,13,15,22,18,31,17,32,15,14,15,0,9,7,6,6,9,6,10,5,8,10,7,7,6,9,0,0,18.8,7.5]
tutorial = [36, 13, 10, 17, 16, 10, 13, 9, 10, 13, 3, 17, 6, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 13.1, 0]
first_loc =[14, 10, 7, 9, 5, 3, 7, 9, 10, 2, 3, 8, 8, 7, 0, 39, 33, 35, 56, 30, 45, 45, 45, 55, 52, 40, 57, 50, 42,0, 0, 7, 45]
first_task = [15, 14, 13, 11, 8, 15, 13, 16, 13, 7, 7, 11, 13, 11, 0, 105, 130, 130, 143, 145, 150, 150, 160, 160, 166, 168, 177, 185, 215,0, 0, 12, 156]
diff_first_task_to_first_loc = np.subtract(first_task,first_loc)
# Heights of bars1 + bars2
FirstLOCWidth = np.add(tutorial, training_task).tolist()
firstTaskWidth = np.add(first_loc, FirstLOCWidth).tolist()
# careful: notice "bottom" parameter became "left"
plt.figure(figsize=(5,5))
p0 = plt.barh(participants, training_task,height=0.8, color="#ffa600")
p1 = plt.barh(participants, tutorial,height=0.8,left=training_task, color="#58508d")
p2 = plt.barh(participants, first_loc,height=0.8, left=FirstLOCWidth, color="#ff6361")
p3 = plt.barh(participants, first_task,height=0.3,left=FirstLOCWidth, color="#003f5c")
# p3 = plt.barh(participants, diff_first_task_to_first_loc, left=firstTaskWidth, color="#003f5c")
# we also need to switch the labels  003f5c
plt.xlabel('Time in minutes', fontsize=12)
# plt.ylabel('Participants of controlled(Ci) and experimental(Ei) groups')
plt.legend((p0[0],p1[0], p2[0], p3[0]),
           ('Tutorials (T0-T1)', '\n'.join(wrap('Learning programming environment (T1-T2)', 25)),
            '\n'.join(wrap('Writing first LOC (T2-T3)', 25)),
'\n'.join(wrap('Writing first microtask or issue (T2-T4)', 25))
            ), fontsize=11)
# plt.title( 'Onboarding time of control(Ci) and experimental(Ei) participants', fontsize=13)
plt.subplots_adjust(left=0.19, right=1.0, top=1.02, bottom=0.1)
# remove the frame

plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)




# plt.show()
plt.savefig('./data/onboading.pdf')

