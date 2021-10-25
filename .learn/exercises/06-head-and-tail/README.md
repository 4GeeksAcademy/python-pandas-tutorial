# File Head and Tail

```python
import pandas as pd

file = pd.read_csv('.learn/assets/pokemon_data.csv')

# we can read just the first 3 rows
print(file.head(3))
```


```python
# or print the last 3 rows
print(file.head(3))
```