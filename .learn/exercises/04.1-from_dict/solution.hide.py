import pandas as pd
# two dimensional array of name,age values.
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
    },
    {
        "brand": "Tesla", 
        "make": "Model S",
        "color": "Red"
    }
]

# create the dataframe and name the columns
df = pd.DataFrame(data)

# print the dataframe
print(df)