import pandas as pd

df = pd.read_csv(r"./NISPUF17.csv")

male_vaccinated = df['VRC1_AGE'].dropna()[df['SEX']==1]
female_vaccinated = df['VRC1_AGE'].dropna()[df['SEX']==2]

dfm = df[df.index.isin(male_vaccinated.index.tolist())]
dff = df[df.index.isin(female_vaccinated.index.tolist())]

prop_male = len(dfm['HAD_CPOX'][dfm['HAD_CPOX']==1])/len(dfm['HAD_CPOX'][dfm['HAD_CPOX']==2])
prop_female = len(dff['HAD_CPOX'][dff['HAD_CPOX']==1])/len(dff['HAD_CPOX'][dff['HAD_CPOX']==2])

stats = {"male":round(prop_male,3),
    "female":round(prop_female,3)}
print(stats)