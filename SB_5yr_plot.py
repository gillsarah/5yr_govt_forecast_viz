import os
import pandas as pd
import matplotlib.pyplot as plt

os.chdir('/Users/Sarah/Desktop')

df = pd.read_csv('SB_5yr_for_py.csv')

fig, ax = plt.subplots(figsize=(8,6))
ax.plot(df['Year'], df['Total Disc Rev'])
ax.plot(df['Year'], df['Expenditures (DGF)'])
plt.show()


fig, ax = plt.subplots(figsize=(8,6))
plt.stackplot(df['Year'], df['Property Tax'], df['Sales Tax'], df['TOT'])
plt.xlabel('Fiscal Year')
plt.ylabel('Revenue Source')
plt.show()


fig, ax = plt.subplots(figsize=(8,6))
ax.bar(df['Year'], df['Other'], color = '#a6cee3', edgecolor='w')
ax.bar(df['Year'], df['Property Tax'], 
        bottom = df['Other'], color = '#1f78b4', edgecolor='w')
ax.bar(df['Year'], df['Sales Tax'], 
        bottom = df['Other']+ df['Property Tax'], color = '#b2df8a',
        edgecolor='w')
ax.bar(df['Year'], df['TOT'], 
        bottom = df['Other']+ df['Property Tax']+ df['Sales Tax'], 
        color = '#33a02c', edgecolor='w')

ax.plot(df['Year'], df['Expenditures (DGF)'], color = '#fdb863')

plt.table()

plt.show()


fig, ax = plt.subplots(figsize=(8,6))
ax.pie([df['Property Tax'][0], df['Sales Tax'][0], df['TOT'][0], df['Other'][0]],
        explode = [0.05, 0.1, 0.1, 0.05],
        labels=df.columns[1:5], autopct='%1.1f%%')
plt.show()



