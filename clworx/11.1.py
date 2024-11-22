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