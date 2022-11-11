# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 16:04:21 2022

@author: admin
"""

# import modules
import matplotlib.pyplot as mp
import pandas as pd
import seaborn as sb

# import file with data
data = pd.read_csv("C:\\pythonprog\\functions1\\bestsellers.csv")

# prints data that will be plotted
# columns shown here are selected by corr() since
# they are ideal for the plot
print(data.corr())

# plotting correlation heatmap
dataplot = sb.heatmap(data.corr(), cmap="YlGnBu", annot=True)

# displaying heatmap
mp.show()
