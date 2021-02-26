import os
import pandas as pd
import matplotlib.pyplot as plt

os.chdir('/Users/Sarah/Documents/Github/5yr_govt_forecast_viz')

df = pd.read_csv('SB_5yr_for_py.csv')

fig, ax = plt.subplots(figsize=(8,6))
ax.plot(df['Year'], df['Total Disc Rev'])
ax.scatter(df['Year'], df['Total Disc Rev'])
ax.plot(df['Year'], df['Expenditures (DGF)'])
ax.scatter(df['Year'], df['Expenditures (DGF)'], color = 'red')
ax.bar(df['Year'], df['Total Disc Rev']-df['Expenditures (DGF)'], 
        bottom = df['Expenditures (DGF)'],
        alpha = 0.5, color = 'yellow')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

ax.set_ylabel('$ in Millions')
plt.title('A Title')
plt.show()


fig, ax = plt.subplots(figsize=(8,6))
plt.stackplot(df['Year'], df['Property Tax'], df['Sales Tax'], df['TOT'])
plt.xlabel('Fiscal Year')
plt.ylabel('Revenue Source')
plt.show()




fig, ax = plt.subplots(figsize=(8,6))
ax.pie([df['Property Tax'][0], df['Sales Tax'][0], df['TOT'][0], df['Other'][0]],
        explode = [0.05, 0.1, 0.1, 0.05],
        labels=df.columns[1:5], autopct='%1.1f%%')
plt.show()



fig, ax = plt.subplots(figsize=(8,6))
ax.bar(df['Year'], df['Other'], color = '#a6cee3', edgecolor='w',
        label = "Other Revenue")
ax.bar(df['Year'], df['Property Tax'], 
        bottom = df['Other'], color = '#1f78b4', edgecolor='w',
        label = 'Property Tax')
ax.bar(df['Year'], df['TOT'], 
        bottom = df['Other']+ df['Property Tax'], 
        color = '#33a02c', edgecolor='w', label = 'TOT')
ax.bar(df['Year'], df['Sales Tax'], 
        bottom = df['Other']+ df['Property Tax']+ df['TOT'],       
        color = '#b2df8a',
        edgecolor='w', label = 'Sales Tax')


#ax.plot(df['Year'], df['Expenditures (DGF)'], color = '#fdb863', label = 'Expenditures')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
#reverse ledgand order #https://stackoverflow.com/questions/34576059/reverse-the-order-of-legend
handles, labels = ax.get_legend_handles_labels()
plt.legend(reversed(handles), reversed(labels), bbox_to_anchor = (1.0, 0.6))
plt.subplots_adjust(right=0.75)
ax.set_ylabel('$ in Millions')
plt.title('A Title')

#maybe label hight?
# #https://stackoverflow.com/questions/30228069/how-to-display-the-value-of-the-bar-on-each-bar-with-pyplot-barh 
plt.savefig('staked_bar_revenue')
#plt.show()






