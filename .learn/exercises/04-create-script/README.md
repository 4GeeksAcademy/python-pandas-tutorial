# Create your script

Let's create our first python script that uses the panda library.

## 📝 Instructions

1. Close the pokemon_data.csv 
2. Create a new `app.py` file in the root of the project, make sure you are in the root.
Your `app.py` file must be next to the `.gitignore`, `learn.json` or `Pipfile` files.
You can also create the file using the terminal command: `$ touch app.py` and open it by double clicking on the file name or typing `$ code app.py`.

2. Type `import pandas` inside the file to import the pandas library.
3. Use the pandas read_csv function to open the CSV file.
4. print the file on the terminal using the `print` function.

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