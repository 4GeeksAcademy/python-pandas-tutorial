# `02.3` Import Pandas

Now let's add Pandas into our script by using the `import` command.

The `import` command is meant for loading 3rd part libraries (like Pandas) or other Python files that you have created (which we will do in the future).

## 📝 Instructions:

1. Type `import pandas as pd` inside the file `app.py` to import the Pandas library.

2. Use the Pandas `read_csv` function to import the content of the CSV file into a variable.

3. Print the variable on the terminal using the `print` function.

## Expected Result:

Run your script and you should see the following output:

![print file](../../assets/print-file.png)

## 💡 Hint:

+ Your code should be something like this

```python
import pandas as pd

data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
print(data_frame)
```

> Note: The `read_csv` function returns something called a `DataFrame`; we will be refering to it as a variable from now on.