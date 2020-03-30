import matplotlib.pyplot as plt
import numpy as np


# year = [2011, 1365, 2016, 2017, 2018, 2019]
year = ["E1", "E2", "E3","E4","E5","E6","E7","E8","E9","E10","E11","E12","E13","E14"
        ,"Mean E1 to E14", "Mean C1 to C14","C1","C2","C3","C4","C5","C6","C7","C8","C9","C10"
        ,"C11","C12","C13","C14"]
tutorial = [36,	13,	10,	17,	16,	10	,13,	9,	10	,13,	3,	17,	6,	11,	13.1,	0,	0,
            0,	0,	0	,0	,0	,0	,0,	0,	0,	0	,0,	0,	0]
first_loc = [14,	10,	7,	9,	5,	3	,7,	9,	10,	2,	3,	8,	8,	7,	7,	45,	39,	33,	35,	56,	30,	45,	45,	45,	55	,52,	40	,57,	50,	42]
first_task = [15,	14,	13,	11,	8,	15,	13,	16,	13,	7,	7,	11,	13,	11,	12,	156,	105,	130,
              130	,143,	145,	150,	150,	160,	160,	166	,168,	177,	185,	215]
# Heights of bars1 + bars2
bars = np.add(tutorial, first_loc).tolist()

p1= plt.barh(year, tutorial, color="#ffa600")
# careful: notice "bottom" parameter became "left"
p2= plt.barh(year, first_loc, left=tutorial, color="#ff6361")
p3= plt.barh(year, first_task, left=bars, color="#58508d")
# we also need to switch the labels
plt.xlabel('Time in minutes')
plt.ylabel('Participants of both conditions')
plt.legend((p1[0], p2[0],p3[0]), ('Time to fetch first task or clone the code', 'Time to write first lines of code'
                                  ,'Times to complete first task'))
plt.title('Onboarding time of participants of both conditions')
# plt.show()
plt.savefig('line_plot.pdf')