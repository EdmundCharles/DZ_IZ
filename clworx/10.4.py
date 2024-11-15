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