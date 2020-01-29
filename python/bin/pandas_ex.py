import pandas as pd

line = '-' * 50

df = pd.read_csv('dbdump.csv')
print(df['IP'])

print(line)

df2 = df['IP'].describe()
print(df2)

print(line)

df3 = df['IP'].describe()
print(df3)

print(line)

df4 = df.describe()
print(df4)
print(line)

df5 = df['ID'].mean()
print('df =', df5)
print(line)

df6 = df.head(5)
df7 = df.tail(5)
print('df6 =', df6)
print(line)
print('df7 =', df7)
print(line)

df8 = df['PICS'].value_counts()
print('df8 =', df8)
print(line)

import matplotlib.pyplot as plt
df8.plot()
plt.show()

df8.plot.bar()
plt.savefig('myGraph.png', bbox_inches='tight')

writer = pd.ExcelWriter('Report.xlsx', engine='xlsxwriter')
df8.to_excel(writer, sheet_name='DATA')
wb = writer.book
ws = wb.add_worksheet('GRAPH')
ws.insert_image('B2', 'myGraph.png')
writer.close()

df9 = df[df['ID'] > 10]
print('df9 =', df9)

df10 = df[df['PICS'].str.endswith('jpg')]
print('df10 =', df10)

df11 = df.groupby(['PICS']).count()
print('df11 =', df11)

# Slicing
df12 = df.iloc[1, 1]    # 1 - cell
df13 = df.iloc[1]   # Row - 1
df14 = df.iloc[:, 1]    # Col - 1
df15 = df.iloc[1:10:2]  # 1 to 9th row step by 2
df16 = df.iloc[:, 0:5:2]    # 0 to 5th col step by 2
df17 = df.iloc[5:10, 1:4]
df18 = df.iloc[[1,4]]
df19 = df.iloc[[1,4], [1,3]]

print('df12', df12, 'df13', df13, 'df14', df14, 'df15', df15, 'df16', df16, 'df17', df17, 'df18', df18, 'df19', df19, sep="\n")