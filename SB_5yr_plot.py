import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set_style('whitegrid')

cmap = sns.cubehelix_palette(start=.5, rot=-.5, as_cmap=True)
#sns.set_palette("BrBG")

#cmap = plt.get_cmap('Spectral')
colors = cmap(np.arange(4)*4)
os.chdir('/Users/Sarah/Documents/Github/5yr_govt_forecast_viz')

df = pd.read_csv('SB_5yr_for_py.csv')

#plot growth or TOT and ST only
def line_plot(var_list, ext_ln = False):
        fig, ax = plt.subplots(figsize=(8,6))
        ax.plot(df['Year'], df[var_list[0]], label = var_list[0])
        ax.plot(df['Year'], df[var_list[1]], label = var_list[1])
        if len(var_list)>=3:
                ax.plot(df['Year'], df[var_list[2]], label = var_list[2])
        if len(var_list)>=4:
                ax.plot(df['Year'], df[var_list[3]], label = var_list[3])
        if ext_ln:
                ax.plot(df['Year'], [10,10,10,10,10], alpha = 0)
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.set_ylabel('$ in Millions')
        plt.legend()
        plt.title('A Title')
        plt.show()

line_plot(df.columns[2:4], ext_ln = True)
line_plot(df.columns[-4:])




fig, ax = plt.subplots(figsize=(10,8))
ax.plot(df['Year'], df['Total Disc Rev'],
        label = 'Revenue')
ax.scatter(df['Year'], df['Total Disc Rev'])
ax.plot(df['Year'], df['Expenditures (DGF)'],
        label = 'Expenditure')
ax.scatter(df['Year'], df['Expenditures (DGF)'], color = 'red')
ax.bar(df['Year'], df['Total Disc Rev']-df['Expenditures (DGF)'], 
        bottom = df['Expenditures (DGF)'],
        alpha = 0.5, color = 'yellow',
        label = 'Surplus')

#for v, i  in enumerate(df['Expenditures (DGF)']):
#        ax.annotate(round(v,2))#, xy = (df['Expenditures (DGF)'][i]))

plt.legend(bbox_to_anchor = (1.0, 0.4))

ax.plot(df['Year'], [175,175,175,175,175], alpha = 0)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.set_ylabel('$ in Millions')
plt.title('A Title')
#plt.show()
plt.savefig('Revenue-Expenditure')


fig, ax = plt.subplots(figsize=(8,6))
plt.stackplot(df['Year'], df['Property Tax'], df['Sales Tax'], df['TOT'])
plt.xlabel('Fiscal Year')
plt.ylabel('Revenue Source')
plt.show()



#Revenue Pie
cmap = sns.cubehelix_palette(start=.5, rot=-.5, as_cmap=True)
def revenue_pie(year):
        fig, ax = plt.subplots(figsize=(8,6))
        ax.pie([df['Property Tax'][year], df['Sales Tax'][year], df['TOT'][year], df['Other'][year]],
                explode = [0.02, 0.12, 0.07, 0.01],
                labels=df.columns[1:5], autopct='%1.1f%%',
                wedgeprops=dict(width=0.55, edgecolor='w'),
                startangle=90,
                counterclock=True,
                colors = cmap([120,30,70,100]))
        plt.title('Revenue by Source {}'.format(df['Year'][year]))
        plt.show()

revenue_pie(0)
revenue_pie(1)
revenue_pie(2)


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






