import pandas as pd

data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')

# We can read only the first 3 rows
print(data_frame.head(3))
