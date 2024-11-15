import pandas as pd
import numpy as np
df = pd.DataFrame({
    'numbers1': [1,1,1,2,3,2,4,232,132],
    'numbers2': [1,234,543,23,43,45,23,1,4],
    'numbers3': [32,23,54,23,65,324,4556,342,34]})
uns = df['numbers1'].compare(df['numbers2'])
print(pd.concat([uns['self'],uns['other']]))