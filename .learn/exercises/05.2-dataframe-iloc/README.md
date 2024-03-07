# `05.2` DataFrame iLoc

The iloc command lets you retrieve any cel in your data_frame. For example, to print the cel in the `x-axis:2` and `y-axis:4` we would have to type the following:

```python
# Print only item in the Row: 2, Col: 4
# remember index starts at 0
print(data_frame.iloc[2,4])
```

## 📝 Instructions:
1. Create a DataFrame using the `.csv` file located at `.learn/assets/pokemon_data.csv`
2. Print the DataFrame row 133 and colum 6 on the screen.

## Expected Result:

Output on the terminal should be `35`.