# `05.5` Print Columns

You can print the column of your choice, for example:

```python
print(data_frame['Type 1'])  # This will print only the column "Type 1"
```

You can also use the square brackets `[]` to pick the range of rows you want to print, like this:

```python
print(data_frame[0:10])
```

Or you can combine both tricks this way:

```python
print(data_frame['Type 1'][0:10])
```

## 📝 Instructions:

1. Use the same DataFrame variable you used in the previous exercise.

2. Print only the columns 'Name' and 'Type 1' from your Dataset, and only the first 10 elements.


## 💻 Expected Result:

Your terminal should look like this:

![Expected result](../../assets/07-print-columns.png)

