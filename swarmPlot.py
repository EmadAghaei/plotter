import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

productivity = pd.read_csv('data/Productivity.csv')
sns.set(style="whitegrid")
# productivity = sns.load_dataset("/Users/emadaghayi/Google Drive/PhD Materials Emad/Microtask Programming/Evaluation  Crowd Microservices/Analysis/workspace/Plotter/data/Productivity.xlsx/Productivity.xlsx")
print(productivity)
ax = sns.violinplot(x="Developers", y="Number of correctly implemented behaviors", data=productivity, inner=None,  palette=['#ff6361','#58508d']).set_title("Productivity of Individual Developers")
ax = sns.swarmplot(x="Developers", y="Number of correctly implemented behaviors", data=productivity, color="white", edgecolor="gray")
plt.savefig('prod.pdf')