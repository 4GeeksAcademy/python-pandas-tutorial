import pandas as pd

data_frame=pd.read_csv('.learn/assets/pokemon_data.csv')
#print(data_frame)

edad=([23,45,7,34,6,63,36,78,54,34])
s1=pd.Series(edad)
#print(s1)

s2 = pd.date_range(start = '2021-05-01', end = '2021-05-12')
#print(s2)

my_series=pd.Series([2,4,6,8,10])
#print(my_series.apply(lambda x: x/2))

data = [["Toyota", "Corolla", "Blue"], ["Ford", "K", "Yellow"], ["Porsche", "Cayenne", "White"]]
dataframe=pd.DataFrame(data,columns=['brand','model','color'])

data = [
    { 
        "brand": "Toyota", 
        "model": "Corolla",
        "color": "Blue"
    },
    {
        "brand": "Ford", 
        "model": "K",
        "color": "Yellow"
    },
    {
        "brand": "Porsche", 
        "model": "Cayenne",
        "color": "White"
    },
    {
        "brand": "Tesla", 
        "model": "Model S",
        "color": "Red"
    }
]

df = pd.DataFrame(data)
#print(df)

#print(data_frame.iloc[133,6])

#print(data_frame.head(3))

#print(data_frame.tail(3))

#print(data_frame[['Name','Type 1']][0:10])

#print(data_frame.loc[data_frame['Attack']>80])

#print(len(data_frame.loc[data_frame['Legendary']==True]))

data_name=pd.read_csv('.learn/assets/us_baby_names_right.csv')
del data_name[data_name.columns[0]]
#print(data_name.head(5))

#print(data_name['Gender'].value_counts())

names = data_name.groupby("Name").sum()
print(len(names))