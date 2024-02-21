import pandas as pd

my_series = pd.Series([2, 4, 6, 8, 10])
modified_series = my_series.apply(lambda x:x/2)

print(modified_series)
