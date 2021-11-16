# Pandas Data Frame from Dictionary

Another way to organize your data before creating a DataFrame will be using dict instead of list.
In this example we have a list of dicts that makes easier to read the data before creating the dataframe.

```python
data = [
    { 
        "brand": "Toyota", 
        "make": "Corolla",
        "color": "Blue"
    },
    {
        "brand": "Ford", 
        "make": "K",
        "color": "Yellow"
    },
    {
        "brand": "Porche", 
        "make": "Cayenne",
        "color": "White"
    }
]
```

## 📝 Instructions

Use this data to create a dataframe but add a new row for a red, Tesla, model S.

## 💻 Expected output

```
    Brand     Make   Color
0  Toyota  Corolla    Blue
1    Ford        K  Yellow
2  Porche  Cayenne   White
3  Tesla   Model S     Red
```