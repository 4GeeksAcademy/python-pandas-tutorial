import pandas as pd

data_frame = pd.read_csv('.learn/assets/us_baby_names_right.csv')
names = data_frame.groupby("Name").sum()

print(len(names))
