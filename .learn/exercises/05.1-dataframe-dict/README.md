# `05.1` DataFrame Dict

Another way to organize your data before creating a DataFrame is to use a `dict` (dictionary) instead of a `list`.

In this example, we have a list of dictionaries that makes it easier to read the data before creating the DataFrame.

```python
data = [
    { 
        "brand": "Toyota", 
        "model": "Corolla",
        "color": "Blue"
    },
    {
        "brand": "Ford", 
        "model": "K",
        "color": "Yellow"
    },
    {
        "brand": "Porsche", 
        "model": "Cayenne",
        "color": "White"
    }
]
```

## 📝 Instructions:

1. Use this data to create a DataFrame but add a new row for a Red, Tesla, Model S.

## 💻 Expected Result:

```bash
     brand    model   color
0   Toyota  Corolla    Blue
1     Ford        K  Yellow
2  Porsche  Cayenne   White
3    Tesla  Model S     Red
```
