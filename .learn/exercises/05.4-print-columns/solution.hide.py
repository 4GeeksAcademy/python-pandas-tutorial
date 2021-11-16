import pandas as pd

data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
print(data_frame[['Name','Type 1']][0:10])