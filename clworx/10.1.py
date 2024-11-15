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