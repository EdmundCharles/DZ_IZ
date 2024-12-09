#Task1
import pandas as pd
import numpy as np
df1 = pd.DataFrame({
    'numbers1': [1,1,1,2,3,2,4,232,132],
    'numbers2': [1,234,543,23,43,45,23,1,4],
    'numbers3': [32,23,54,23,65,324,4556,342,34]})
print(df1)



df2 = pd.DataFrame([1,2,3,4,5,6,7,8,'ggg','dsd','s','f'], columns=['numbers'])
print(df2)


array = np.array([1,2,3,4,5,6,7,8])
df3 = pd.DataFrame(array,columns=['nums'])
print(df3)
#Task2
import pandas as pd
import numpy as np
df = pd.DataFrame({
    'numbers1': [1,1,1,2,3,2,4,232,132],
    'numbers2': [1,234,543,23,43,45,23,1,4],
    'numbers3': [32,23,54,23,65,324,4556,342,34]})
uns = df['numbers1'].compare(df['numbers2'])
print(pd.concat([uns['self'],uns['other']]))
#Task3
import pandas as pd
from matplotlib import pyplot as plt

# Данные
dt = {
    'id': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10, 10: 11, 11: 12,
           12: 13, 13: 14, 14: 15, 15: 16, 16: 17, 17: 18, 18: 19, 19: 20, 20: 21, 21: 22,
           22: 23, 23: 24, 24: 25, 25: 26, 26: 27, 27: 28, 28: 29, 29: 30, 30: 31, 31: 32, 32: 33,
           33: 34, 34: 35},
    'name': {0: 'John Deo', 1: 'Max Ruin', 2: 'Arnold', 3: 'Krish Star', 4: 'John Mike',
             5: 'Alex John', 6: 'My John Rob', 7: 'Asruid', 8: 'Tes Qry', 9: 'Big John',
             10: 'Ronald', 11: 'Recky', 12: 'Kty', 13: 'Bigy', 14: 'Tade Row', 15: 'Gimmy',
             16: 'Tumyu', 17: 'Honny', 18: 'Tinny', 19: 'Jackly', 20: 'Babby John', 21: 'Reggid',
             22: 'Herod', 23: 'Tiddy Now', 24: 'Giff Tow', 25: 'Crelea', 26: 'Big Nose',
             27: 'Rojj Base', 28: 'Tess Played', 29: 'Reppy Red', 30: 'Marry Toeey',
             31: 'Binn Rott', 32: 'Kenn Rein', 33: 'Gain Toe', 34: 'Rows Noump'},
    'class': {0: 'Four', 1: 'Three', 2: 'Three', 3: 'Four', 4: 'Four', 5: 'Four',
              6: 'Five', 7: 'Five', 8: 'Six', 9: 'Four', 10: 'Six', 11: 'Six', 12: 'Seven',
              13: 'Seven', 14: 'Four', 15: 'Four', 16: 'Six', 17: 'Five', 18: 'Nine', 19: 'Nine',
              20: 'Four', 21: 'Seven', 22: 'Eight', 23: 'Seven', 24: 'Seven', 25: 'Seven',
              26: 'Three', 27: 'Seven', 28: 'Seven', 29: 'Six', 30: 'Four', 31: 'Seven', 32: 'Six',
              33: 'Seven', 34: 'Six'},
    'mark': {0: 75, 1: 85, 2: 55, 3: 60, 4: 60, 5: 55, 6: 78,
             7: 85, 8: 78, 9: 55, 10: 89, 11: 94, 12: 88, 13: 88, 14: 88, 15: 88, 16: 54, 17: 75,
             18: 18, 19: 65, 20: 69, 21: 55, 22: 79, 23: 78, 24: 88, 25: 79, 26: 81, 27: 86, 28: 55,
             29: 79, 30: 88, 31: 90, 32: 96, 33: 69, 34: 88},
    'gender': {0: 'female', 1: 'male', 2: 'male', 3: 'female', 4: 'female', 5: 'male',
               6: 'male', 7: 'male', 8: 'male', 9: 'female', 10: 'female', 11: 'female', 12: 'female',
               13: 'female', 14: 'male', 15: 'male', 16: 'male', 17: 'male', 18: 'male', 19: 'female',
               20: 'female', 21: 'female', 22: 'male', 23: 'male', 24: 'male', 25: 'male', 26: 'female',
               27: 'female', 28: 'male', 29: 'female', 30: 'male', 31: 'female', 32: 'female',
               33: 'male', 34: 'female'}
}

# Создаем DataFrame
df = pd.DataFrame(data=dt)
df.set_index(["gender", 'class'], inplace=True)

grouped = df.groupby(['mark']).size()

plt.bar(grouped.index,grouped.values,color='blue')
plt.xlabel('Marks')
plt.ylabel('Number of students')
plt.title('Marks distribution')
plt.grid(axis='y',linestyle='--',alpha=0.5)
plt.tight_layout()
plt.show()
#Task4
import pandas as pd
import numpy as np
df1 = pd.DataFrame({
    'numbers1': [1,1,1,2,3,2,4,232,132],
    'numbers2': [1,234,543,23,43,45,23,1,4],
    'numbers3': [32,23,54,23,65,324,4556,342,34]})
df2 = pd.DataFrame({
    'numbers4': [1,2,344,65,243,35,234,23,54],
    'numbers5': [9,8,7,6,5,4,32,1,3],
    'numbers6': [4,54,23,234,234,321,123,65,34]
})
df3=pd.concat([df1,df2],axis=0)
df3 = df3.fillna(0)
print(df3)

df4=pd.concat([df1,df2],axis=1)
print(df4)
#Task5
import pandas as pd
from matplotlib import pyplot as plt

df = pd.DataFrame({
    'age' : [i for i in range(0,13)],
    'weight_normal' : [3.4,4.3,5.1,5.8,6.5,7.1,7.6,8.2,8.6,9.1,9.5,9.8,10],
    'heavier_side' : [4.2,5.4,6.4,7.3,8.1,8.8,9.4,9.9,10.5,11,11.4,11.8,12.4],
    'lighter_side' : [2.7,3.3,3.9,4.5,5.1,5.6,6.1,6.6,7.1,7.5,8.2,8.5,9.1]
})

plt.plot(df['age'],df['weight_normal'],color='green',label='Average')
plt.plot(df['age'],df['heavier_side'],color='red',label='Heavier')
plt.plot(df['age'],df['lighter_side'],color='blue',label='Lighter')
plt.xlim(0,12)
plt.ylim(0,13)
plt.ylabel('Weight')
plt.xlabel('Age')
plt.title('Toddler weight depending on age and build')
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()