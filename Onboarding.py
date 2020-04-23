import matplotlib.pyplot as plt
import numpy as np
from textwrap import wrap
import matplotlib as mpl


participants = ["E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9", "E10", "E11", "E12", "E13", "E14", "", "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14", " "
  ," "  , "Mean E1-14", "Mean C1-14"]
# addedd zero as seperator
training_task=[30,10,17,15,13,15,22,18,31,17,32,15,14,15,0,9,7,6,6,9,6,10,5,8,10,7,7,6,9,0,0,18.8,7.5]
tutorial = [36, 13, 10, 17, 16, 10, 13, 9, 10, 13, 3, 17, 6, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 13.1, 0]
first_loc =[14, 10, 7, 9, 5, 3, 7, 9, 10, 2, 3, 8, 8, 7, 0, 39, 33, 35, 56, 30, 45, 45, 45, 55, 52, 40, 57, 50, 42,0, 0, 7, 45]
first_task = [15, 14, 13, 11, 8, 15, 13, 16, 13, 7, 7, 11, 13, 11, 0, 105, 130, 130, 143, 145, 150, 150, 160, 160, 166, 168, 177, 185, 215,0, 0, 12, 156]
# Heights of bars1 + bars2
FirstLOCWidth = np.add(tutorial, training_task).tolist()
firstTaskWidth = np.add(first_loc, FirstLOCWidth).tolist()
# careful: notice "bottom" parameter became "left"
# plt.figure(figsize=(5,7))
p0 = plt.barh(participants, training_task, color="#ffa600")
p1 = plt.barh(participants, tutorial,left=training_task, color="#ff6361")
p2 = plt.barh(participants, first_loc, left=FirstLOCWidth, color="#58508d")
p3 = plt.barh(participants, first_task, left=firstTaskWidth, color="#003f5c")
# we also need to switch the labels  003f5c
plt.xlabel('Time in minutes', fontsize=12)
# plt.ylabel('Participants of controlled(Ci) and experimental(Ei) groups')
plt.legend((p0[0],p1[0], p2[0], p3[0]),
           ('Training task', '\n'.join(wrap('Beginning of session until starting the first task', 25)),
            '\n'.join(wrap('Start first task/issue until writing first LOC', 25)),
'\n'.join(wrap('Start first task/issue until finishing it', 25))
            ), fontsize=11)
plt.title( 'Onboarding time of control(Ci) and experimental(Ei) participants', fontsize=13)
plt.subplots_adjust(left=0.19, right=0.89, top=0.87, bottom=0.1)
# remove the frame

plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
# plt.figure(figsize=(5,5))



# plt.show()
plt.savefig('./data/onboading.pdf')

