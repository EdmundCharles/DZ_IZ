#Task1
import pandas as pd

df = pd.read_csv(r"./NISPUF17.csv")

def proportion_of_education(dataframe):

    len_of_df = len(df)
    less_then_12 = round(float(df['EDUC1'].where(df['EDUC1']==1).count()/len_of_df),2)
    exactly_12 = round(float(df['EDUC1'].where(df['EDUC1']==2).count()/len_of_df),2)
    more_than_12 = round(float(df['EDUC1'].where(df['EDUC1']==3).count()/len_of_df),2)
    college = round(float(df['EDUC1'].where(df['EDUC1']==4).count()/len_of_df),2)

    dict =  {"less than high school": less_then_12,
    "high school":exactly_12,
    "more than high school but not college":more_than_12,
    "college":college}

    print(dict)

proportion_of_education(df)
#Task2
import pandas as pd

df = pd.read_csv(r"./NISPUF17.csv")

bm = df.groupby('CBF_01')['P_NUMFLU'].mean()

bm_tuple = [round(float(bm[1]),1),round(float(bm[2]),1)]

print(bm_tuple)
#Task3
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