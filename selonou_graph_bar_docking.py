import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv("output_hypothetical_docking_score.csv")
N = 260
df = pd.Series(np.random.randint(210,250,N), index=np.arange(1,N+1))
cmap = plt.cm.tab10
colors = cmap(np.arange(len(df)) % cmap.N)
df.plot.bar(color=colors)  # or df.plot.barh(color=colors)   for horizontal bar
plt.savefig("selonou_graph_6.png")
