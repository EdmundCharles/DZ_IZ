import pandas as pd

df = pd.read_csv(r"./NISPUF17.csv")

bm = df.groupby('CBF_01')['P_NUMFLU'].mean()

bm_tuple = [round(float(bm[1]),1),round(float(bm[2]),1)]

print(bm_tuple)