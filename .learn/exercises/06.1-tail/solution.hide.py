import pandas as pd

data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')

# we can read just the first 3 rows
print(data_frame.tail(3))