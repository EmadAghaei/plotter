import matplotlib.pyplot as plt
import numpy as np




qos_metrics = [ "Simplicity_E","Simplicity_C","Consistency_E" ,"Consistency_C", "Clarity_E","Clarity_C" ]
Poor = [0.0,8.9,12.5,12.5,0.0,10.7]
Fair =[25.0,12.5,12.5,12.5,0.0,21.4]
Satisfactory = [0.0,30.4,0.0,17.9,37.5,28.6]
Very_Good = [62.5,25.0,50.0,32.1,50.0,19.6]
Excellent =[12.5,23.2,25.0,25.0,12.5,19.6]
# Heights of bars1 + bars2
SatisfactoryLeft = np.add(Poor, Fair).tolist()
VeryGoodLeft = np.add(SatisfactoryLeft, Satisfactory).tolist()
ExcellentLeft = np.add(VeryGoodLeft, Very_Good).tolist()

p1= plt.barh(qos_metrics, Poor, color="#ffa600")
# careful: notice "bottom" parameter became "left"
p2= plt.barh(qos_metrics, Fair, left=Poor, color="#ff6361")
p3= plt.barh(qos_metrics, Satisfactory, left=SatisfactoryLeft, color="#bc5090")
p4= plt.barh(qos_metrics, Very_Good, left=VeryGoodLeft, color="#58508d")
p5= plt.barh(qos_metrics, Excellent, left=ExcellentLeft, color="#003f5c")

# we also need to switch the labels
plt.xlabel('Percent')
# plt.ylabel('Participants of controlled(Ci) and experimental(Ei) groups')
plt.legend((p1[0], p2[0],p3[0],p4[0],p5[0]), ('Poor', 'Fairs','Satisfactory','Very Good','Excellent'),loc='lower left',
           bbox_to_anchor=(0,1.02,1, 0.2),mode='expand',ncol=5,borderaxespad=0)
plt.title('Quality of code by controlled (C) and experimental (E) groups',y=1.09)
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
plt.show()
plt.savefig('./data/Qoc.pdf',bbox_inches='tight')