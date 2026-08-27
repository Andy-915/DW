import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame({
  'aquarium': ['Monterrey Bay', 'Georgia Aquarium', 'Shedd Aquarium', 'National Aquarium'],
  'shark': [5, 4, 4, 2],
  'dolphin': [8, 12, 10, 5],
  'octopus': [7, 20, 8, 4],
  'sea turtle': [12, 5, 6, 3],
  'jellyfish': [30, 25, 20, 15]
})
plt.figure()
plt.bar(df['aquarium'], df['shark'], label = 'Shark' , color= 'blue' )
plt.bar(df['aquarium'], df['dolphin'], label = 'Dolphin' , color= 'red' )
plt.bar(df['aquarium'], df['sea turtle'], label = 'Sea Turtle' , color= 'brown' )
plt.bar(df['aquarium'], df['jellyfish'], label = 'Jellyfish' , color= 'orange' )
plt.legend()
plt.title('Number of Animals in Aquariams')
plt.xlabel('Aquarium')
plt.ylabel('Number of Animals')
plt.show()


fig, axes= plt.subplots(2,2,figsize = (10,10), sharex= True)
axes[0,0].plot(df['Exam'],df['Alice'], color = 'green', label = 'Alice')
axes[0,0].set_title('Grades of Alice')
axes[0,0].set_ylabel('Grade')
axes[0,0].legend()
axes[0,0].set_xlabel('Subject')
axes[0,1].plot(df['Exam'],df['Bob'], color = 'skyblue', label = 'Bob')
axes[0,1].set_title('Grades of Bob')
axes[0,1].set_ylabel('Grade')
axes[0,1].legend()
axes[0,1].set_xlabel('Subject')
axes[1,0].plot(df['Exam'],df['Charlie'], color = 'pink', label = 'Charlie')
axes[1,0].set_title('Grades of Charlie')
axes[1,0].set_ylabel('Grade')
axes[1,0].legend()
axes[1,0].set_xlabel('Subject')
axes[1,1].plot(df['Exam'],df['Diana'], color = 'olive', label = 'Diana')
axes[1,1].set_title('Grades of Diana')
axes[1,1].set_ylabel('Grade')
axes[1,1].legend()
axes[1,1].set_xlabel('Subject')
plt.show()

import pandas as pd
df = pd.read_csv('./data/gas_electricity_rent_expenses.csv')
df
fig, ax = plt.subplots(figsize=(10, 10))

months = df['Month'].unique()

for month in months:
  month_data = df[df['Month'] == month]
  ax.plot(
    month_data['Month'],
    month_data['Amount_USD'],
    marker='D',
    label=month
  )

ax.set_title('Monthly Expenses for Gas, Electricity & Rent')
ax.set_xlabel('Month')
ax.set_ylabel('Amount (USD)')
ax.legend()

plt.show()


fig, ax = plt.subplots(figsize=(10, 10))

category = df['Category'].unique()

for c in category:
  month_data = df[df['Category'] == c]
  ax.plot(
    month_data['Month'],
    month_data['Amount_USD'],
    marker='D',
    label=c
  )

ax.set_title('Monthly Expenses for Gas, Electricity & Rent')
ax.set_xlabel('Month')
ax.set_ylabel('Amount (USD)')
ax.legend()

plt.show()