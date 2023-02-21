import pandas as pd
import seaborn as sns
import numpy as np

df = pd.read_csv('athlete_events.csv')
df.shape
list(df)

#Renvoie le pourcentage des valeurs incomplètes
def NaN_percent(df, column_name) :
    row_count = df[column_name].shape[0]
    empty_values = row_count - df[column_name].count()
    return (100.0*empty_values)/row_count
for i in list(df):
    print(i + ": " + str(NaN_percent(df,i))+"%")
    
male_df = df[df.Sex=='M']
sport_weight_height_metrics = male_df.groupby(['Sport'])['Weight','Height'].agg(['min','max','mean'])

sport_weight_height_metrics.Weight.dropna().sort_values('mean', ascending=False)


sns.displot(sport_weight_height_metrics.Height.dropna()['mean'])

#total_rows = df.shape[0]
#unique_athletes = len(df.name.unique())
#medal_winners = len(df[df.Medal.fillna("None") != "None"].Name.unique())

#"{0} {1} {2}".format(total_rows, unique_athletes, medal_winners)