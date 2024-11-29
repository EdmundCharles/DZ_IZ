
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#Task1
df = pd.read_csv(r'./Mall_Customers.csv')

by_gender = df.groupby('Genre')['Annual Income (k$)'].mean()

print(by_gender['Female'])

#Task2

by_expenses = df.groupby('Genre')[['Spending Score (1-100)','CustomerID']].max()

print(by_expenses)

#Task3

men = df[df['Genre']=='Male']
men_income = men[['Age','Annual Income (k$)']].set_index('Age')

men_income.plot(style='o',ylabel='Annual income',xlabel='Age',title='Income depending on age for men',grid=True,color='black')
plt.show()

#Task4

data_female = df[df['Genre']=='Female'].set_index('Annual Income (k$)').groupby('Annual Income (k$)')['Spending Score (1-100)'].mean()
data_male = df[df['Genre']=='Male'].set_index('Annual Income (k$)').groupby('Annual Income (k$)')['Spending Score (1-100)'].mean()

data = pd.DataFrame({'Feamale':data_female, 'Male':data_male})
data.plot.bar(ylabel='Spending Score (1-100)')
plt.show()