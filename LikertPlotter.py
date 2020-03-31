import pandas as pd
import xlrd as xlrd
# import plot_likert
import numpy as np
from plot_likert import *
from plot_likert.scales import *

from pathlib import Path

path = Path(__file__).parent / "./data/Qoc.csv"


# data=pd.read_csv(path,converters={"Poor":int,"Fair":int, "Satisfactory":int,  "Very good":int,  "Excellent":int})
data=pd.read_csv(path)
print(data)

data = pd.DataFrame(np.random.choice(agree, (10,2)), columns=['q1','q2'])
# print(data)
percentages = likert_percentages(data, agree)

plot_counts(percentages, agree, plot_percentage=True)