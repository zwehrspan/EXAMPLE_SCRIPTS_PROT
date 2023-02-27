import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read in data
inData = pd.read_csv("DATA/diff.txt", delim_whitespace=True)

# Calculate ratios
inData['initialdTransRatio'] = inData['dTransCalcR1'] / inData['dTransHydro']
inData['finaldTransRatio'] = inData['dTransCalcR2'] / inData['dTransHydro']
inData['initialdRotRatio'] = inData['dRotCalcR1'] / inData['dRotHydro']
inData['finaldRotRatio'] = inData['dRotCalcR2'] / inData['dRotHydro']
inData['fakeName'] = inData['UniProtID']
inData = inData.sort_values(by='initialdTransRatio')

# Plot Translation
my_range=range(1,len(inData.index)+1)
plt.hlines(y=my_range, xmin=inData['initialdTransRatio'], xmax=inData['finaldTransRatio'], color='grey', alpha=0.4)
plt.scatter(inData['initialdTransRatio'], my_range, color='skyblue', alpha=1, label='Initial')
plt.scatter(inData['finaldTransRatio'], my_range, color='green', alpha=0.4 , label='Final')
plt.legend()
plt.yticks(my_range, inData['UniProtID'])
plt.title("Comparison of the D_trans ratio before and after adjustment", loc='center')
plt.xlabel('D_trans Simulation / D_trans Experiment')
plt.ylabel('Protein Name')
plt.show()
plt.clf()

# Plot Rotation
my_range=range(1,len(inData.index)+1)
plt.hlines(y=my_range, xmin=inData['initialdRotRatio'], xmax=inData['finaldRotRatio'], color='grey', alpha=0.4)
plt.scatter(inData['initialdRotRatio'], my_range, color='skyblue', alpha=1, label='Initial')
plt.scatter(inData['finaldRotRatio'], my_range, color='green', alpha=0.4 , label='Final')
plt.legend()
plt.yticks(my_range, inData['UniProtID'])
plt.title("Comparison of the D_rot ratio before and after adjustment", loc='center')
plt.xlabel('D_rot Simulation / D_rot Experiment')
plt.ylabel('Protein Name')
plt.show()
plt.clf()

# Plot relationship between translation and rotation initial
plt.plot('initialdTransRatio', 'initialdRotRatio', data = inData, linestyle = 'none', marker = "o", color='red', alpha=1)
plt.title("Comparison of the initial D_trans and D_rot ratios", loc='center')
plt.xlabel('D_trans Ratio Initial')
plt.ylabel('D_rot Ratio Initial')
m, b = np.polyfit(inData['initialdTransRatio'], inData['initialdRotRatio'], 1)
# Plot regression line
plt.axline(xy1=(0,b), slope = m, linestyle = "--", color = "k")
plt.show()
plt.clf()



plt.hist('finaldTransRatio', data = inData, edgecolor="black")
plt.title("Distribution of Final D_trans ratios", loc='center')
plt.ylabel('Counts')
plt.xlabel('D_trans Ratio Final')
plt.show()
plt.clf()

plt.hist('finaldRotRatio', data = inData, edgecolor="black", bins = 50)
plt.title("Distribution of Final D_rot ratios", loc='center')
plt.ylabel('Counts')
plt.xlabel('D_rot Ratio Final')
plt.show()
plt.clf()
