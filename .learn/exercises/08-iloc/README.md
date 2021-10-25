# Using the iloc function in pandas

```python
import pandas as pd

file = pd.read_csv('.learn/assets/pokemon_data.csv')

# Print only item in the Row: 2, Col: 1
# remember index starts at 0
print(file.iloc[2,1])
```