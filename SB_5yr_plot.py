import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#sns.set_style('white')

cmap = sns.cubehelix_palette(start=.5, rot=-.5, as_cmap=True)
#sns.set_palette('PuBu')

#cmap = plt.get_cmap('')
colors = cmap(np.arange(4)*4)
os.chdir('/Users/Sarah/Documents/Github/5yr_govt_forecast_viz')

df = pd.read_csv('SB_5yr_for_py.csv')

#plot growth
def line_plot(var_list, y_axis, ext_ln = False):
        fig, ax = plt.subplots(figsize=(8,6))
        ax.plot(df['Year'], df[var_list[0]], label = var_list[0])
        ax.plot(df['Year'], df[var_list[1]], label = var_list[1])
        if len(var_list)>=3:
                ax.plot(df['Year'], df[var_list[2]], label = var_list[2])
        if len(var_list)>=4:
                ax.plot(df['Year'], df[var_list[3]], label = var_list[3])
        if ext_ln:
                ax.plot(df['Year'], [10]*len(df['Year']), alpha = 0)
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.set_ylabel(y_axis)
        ax.set_xlabel('Fiscal Year')
        plt.legend()
        #plt.title('A Title')
        plt.show()

line_plot(df.columns[2:4], '', ext_ln = True)
line_plot(df.columns[-4:], "% Annual Growth")



# Surpluss Line
def account_balance_line(revenue, expenditure, rev_label = 'Revenue', 
                         rev_color = '#034e7b', save_name = 'surplus_line',
                         bbox = (1.1, 0.4), surplus = False):
        fig, ax = plt.subplots(figsize=(8,6))
        ax.plot(df['Year'], revenue,
                label = rev_label, color = rev_color)
        ax.scatter(df['Year'], revenue, color = '#034e7b')
        ax.plot(df['Year'], expenditure,
                label = 'Expenditure', color = '#a6bddb')
        ax.scatter(df['Year'], expenditure, color = '#a6bddb')
        
        if surplus:     
                ax.bar(df['Year'], revenue - expenditure, 
                        bottom = expenditure,
                        alpha = 0.5, color = '#fec44f',
                        edgecolor = '#fe9929',
                        label = 'Surplus')
                position = 'Surplus'
        else:
                ax.bar(df['Year'], revenue - expenditure, 
                        bottom = expenditure,
                        alpha = 0.5, color = '#fb6a4a',
                        edgecolor = '#ef3b2c',
                        label = 'Deficit')
                position = 'Deficit'

        # annotate the account position
        for i, v in enumerate(revenue - expenditure):
                #if v != 0: 
                ax.annotate('${}M'.format(round(v,2)), 
                        (revenue[i] - 0.45*(revenue[i] - expenditure[i])),
                                horizontalalignment='center', verticalalignment='center',
                                fontsize = 8, weight="bold")

        plt.legend(bbox_to_anchor = bbox)
        # allow for some space on top and bottom
        plt.ylim((revenue.min()-20,revenue.max()+10))
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.set_ylabel('$ in Millions')
        ax.set_xlabel('Fiscal Year')
        plt.title('Forecasted Financial Position\n{}'.format(position))
        plt.show()
        #plt.savefig(save_name)

account_balance_line(df['Total Disc Rev'], df['Expenditures (DGF)'], 
                        bbox=(0.99,0.3))
#surplus_line(df['Total w/o Other'], df['Surplus w/o Other Rev'], 
#                'Revenue (Top 3 Sources Only)','#006d2c', 'top-3-rev-surplus',
#                (0.99,0.3), True)

fig, ax = plt.subplots(figsize=(8,6))
plt.stackplot(df['Year'], df['Property Tax'], df['Sales Tax'], df['TOT'])
plt.xlabel('Fiscal Year')
plt.ylabel('Revenue Source')
plt.show()



#Revenue Pie
cmap = sns.cubehelix_palette(start=.5, rot=-.5, as_cmap=True)
labels = ['Property Tax', 'TOT', 'Sales Tax', 'Other']
def revenue_pie(year, labels):
        fig, ax = plt.subplots(figsize=(8,6))
        ax.pie([df[labels[0]][year], df[labels[1]][year], df[labels[2]][year], df[labels[3]][year]],
                explode = [0.02, 0.12, 0.07, 0.01],
                wedgeprops=dict(width=0.55, edgecolor='w'),
                startangle=90,
                counterclock=True,
                colors = cmap([120,30,70,100]),
                labels=labels, 
                autopct='%1.1f%%')
        plt.title('Revenue by Source {}'.format(df['Year'][year]))
        #plt.savefig('pie')
        plt.show()

revenue_pie(0, labels)
revenue_pie(1, labels)
revenue_pie(2, labels)

def nested_pie(year):
        width = 0.3
        fig, ax = plt.subplots(figsize=(8,6)) 
        ax.pie([df['Total Disc Rev'][year]],
                #labels = ['Revenue'],
                radius = 1,
                wedgeprops = dict(width=width, edgecolor='w'),
                colors = cmap([120]))
        ax.pie([df['Expenditures (DGF)'][year], df['Total Disc Rev'][year]- df['Expenditures (DGF)'][year]],
                #labels = ['Expenditures', 'Surplus'],
                radius = 1 - width,
                wedgeprops = dict(width=width, edgecolor='w'),
                colors = ['#a6bddb', '#fec44f'])
        plt.title('General Fund Discretionary Revenue and Expenditures {}'.format(df['Year'][year]))
        plt.savefig('nested pie')
        #plt.show()

nested_pie(0)
 
plt.pie([df['Total Disc Rev'][0]])
plt.show()


#Revenue by source stacked bar
def stacked_bar(show_expenditure = False):
        fig, ax = plt.subplots(figsize=(8,6))
        ax.bar(df['Year'], df['Other'], 
                color = cmap([150]), #'#3182bd', #'#a6cee3', #edgecolor='w',
                label = "Other Revenue")
        ax.bar(df['Year'], df['Property Tax'], 
                bottom = df['Other'], 
                color = cmap([130]), #'#6baed6', #'#1f78b4', #edgecolor='w',
                label = 'Property Tax')
        ax.bar(df['Year'], df['Canabus Tax'],
                bottom = df['Other']+ df['Property Tax'],
                color = cmap([100]),
                label = 'Canabus Tax')
        ax.bar(df['Year'], df['TOT'], 
                bottom = df['Other']+ df['Property Tax']+ df['Canabus Tax'], 
                color = cmap([60]), #'#9ecae1', #'#33a02c', #edgecolor='w', 
                label = 'TOT')
        ax.bar(df['Year'], df['Sales Tax'], 
                bottom = df['Other']+ df['Property Tax']+ df['TOT']+ df['Canabus Tax'],       
                color = cmap([30]), #'#c6dbef', #'#b2df8a', #edgecolor='w', 
                label = 'Sales Tax')
        if show_expenditure:
                ax.plot(df['Year'], df['Expenditures (DGF)'], color = '#fec44f', label = 'Expenditures')
                ax.scatter(df['Year'], df['Expenditures (DGF)'], s = 20, color = '#fec44f')
        #ax.plot(df['Year'], df['Total Disc Rev'], color  = '#02818a', label = 'Total Revenue')
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        #reverse ledgand order #https://stackoverflow.com/questions/34576059/reverse-the-order-of-legend
        handles, labels = ax.get_legend_handles_labels()
        plt.legend(reversed(handles), reversed(labels), bbox_to_anchor = (1.0, 0.6))
        plt.subplots_adjust(right=0.75)
        ax.set_ylabel('$ in Millions')
        ax.set_xlabel('Fiscal Year')
        #plt.title('A Title')

        #maybe label hight?
        # #https://stackoverflow.com/questions/30228069/how-to-display-the-value-of-the-bar-on-each-bar-with-pyplot-barh 
        #plt.savefig('staked_bar_revenue')
        #plt.savefig('staked_bar_blue')
        plt.show()

stacked_bar()
stacked_bar(show_expenditure = True)

#broke it -not sure why, but doesn't run with plot anymore
def add_table():
        # https://matplotlib.org/stable/gallery/misc/table_demo.html
        the_table = plt.table(cellText=[round(df['Property Tax'],2), round(df['Other'],2),
                                round(df['Canabus Tax'],2), round(df['TOT'],2), round(df['Sales Tax'],2)],
                                rowLabels=['Property Tax', 'Other', 'Canabus Tax','TOT', 'Sales Tax'],
                                rowColours=cmap([130, 150, 100, 60, 30]),
                                colLabels=df['Year'],
                                loc='bottom')
        # Adjust layout to make room for the table:
        plt.subplots_adjust(left=0.2, bottom=0.2)
        plt.xticks([])

def run_stacked_bar(show_expenditure = False, table = False, savefig = False, save_as = ''):
        stacked_bar(show_expenditure = show_expenditure)
        if table:
           add_table()  
        if savefig:
                plt.savefig(save_as) 
        else:
                plt.show()

run_stacked_bar(show_expenditure = True, savefig = True, save_as = 'test')
run_stacked_bar(show_expenditure = True)
run_stacked_bar(table = True)
run_stacked_bar(table = True, savefig = True, save_as = 'test')






