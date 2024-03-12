import pandas as pd

data_frame = pd.read_csv('.learn/assets/us_baby_names_right.csv')
count = data_frame['Gender'].value_counts()

print(count)
