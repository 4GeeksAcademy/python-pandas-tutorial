# Create your script

Now let's add Pandas into our script by using the `import` command.

The `import` command is meant for loading 3rd part libraries (like pandas) or other python files that you have created (which we will do in the future)

## 📝 Instructions

1. Type `import pandas as pd` inside the file to import the pandas library.
2. Use the pandas read_csv function to import the content of the CSV file into a variable.
3. print the variable on the terminal using the `print` function.

## 💡 Your code should be something like this

```python
import pandas as pd

data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
print(data_frame)
```

Note:  the read_csv function returns something called a `DataFrame`, we will be referring to that `data_frame` variable from now on.

## Compare your output

After you run the command you should see something like this:

![print file](../../assets/print-file.png)