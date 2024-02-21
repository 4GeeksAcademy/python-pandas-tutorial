import pandas as pd

data_frame = pd.read_csv('.learn/assets/us_baby_names_right.csv')
del data_frame[data_frame.columns[0]]

print(data_frame.head(5))
