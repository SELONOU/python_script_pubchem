import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("test_head_Results_docking_hypothetical_compounds.csv", sep=",")
#####################################groupby hypothetical column to get the minimum values according to Docking_score values
df1=df.groupby('hypothetical').Docking_score.min()
print(df1)
df1.to_csv('output_hypothetical_docking_score.csv')

##################################### use describe to get max, min, count, mean or median 
df2=df.groupby('hypothetical').Docking_score.agg(['count', 'min', 'max', 'mean'])  # or print(df1.describe())
print(df2)
##################################### plot the docking_score values
fig = df.groupby('hypothetical').min().plot(kind='bar')
plt.savefig("mol_vs_figure_docking_score_1.png")
##################################### plot with colors
fig = df.groupby('hypothetical').min().plot(kind='bar', color=(1.0, 0.0, 0.0, 0.2))
plt.savefig("mol_vs_figure_docking_score_2.png")
##################################### 
d0 = df.groupby('hypothetical').min()
fig=plt.figure(figsize=(20,10))
ax1=plt.subplot(111)
ax1.barh(df['hypothetical'], df['Docking_score'])
plt.savefig("mol_vs_figure_docking_score_3.png")
#####################################
df001=pd.read_csv("output_hypothetical_docking_score.csv")
hypothetical=df001.hypothetical
Docking_score=df001['Docking_score']
plt.bar(hypothetical,Docking_score)
plt.xlabel('hypothetical')
plt.ylabel('Docking_score')
plt.title('selonou_graph')
plt.savefig("mol_vs_figure_docking_score_4.png")
###############differents colors
import numpy as np
N = 260
df = pd.Series(np.random.randint(210,250,N), index=np.arange(1,N+1))
cmap = plt.cm.tab10
colors = cmap(np.arange(len(df)) % cmap.N)
df001.plot.bar(color=colors)  # or df.plot.barh(color=colors)   for horizontal bar
plt.savefig("mol_vs_figure_docking_score_5.png")
###############################
N = 260
df = pd.Series(np.random.randint(210,250,N), index=np.arange(1,N+1))
cmap = plt.cm.tab10
colors = cmap(np.arange(len(df)) % cmap.N)
df001.plot.barh(color=colors)  # or df.plot.barh(color=colors)   for horizontal bar
plt.savefig("mol_vs_figure_docking_score_6.png")


