import pandas as pd

data_frame=pd.read_csv('.learn/assets/pokemon_data.csv')
#print(data_frame)

edad=([23,45,7,34,6,63,36,78,54,34])
s1=pd.Series(edad)
#print(s1)

s2=pd.date_range(start='2021-05-01',end='2021-02-12')
print(s2)