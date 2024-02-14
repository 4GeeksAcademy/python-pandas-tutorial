# `02.2` Import 

Now let's add Pandas into our script by using the `import` command.

The `import` command is meant for loading 3rd-party libraries (like Pandas) or other Python files that you have created (which we will do in the future).

## 📝 Instructions:

1. Type `import pandas as pd` inside the file `app.py` to import the Pandas library.

2. Create a variable called `data_frame`.

3. Use the Pandas `read_csv` function to import the contents of a CSV file in this path `.learn/assets/pokemon_data.csv`; assign it to the variable `data_frame`.

4. Print the variable on the terminal using the `print` function.

## 💻 Expected Result:

Run your script, and you should see the following output:

![Run app.py file](../../assets/print-file.png)

## 💡 Hint:

+ Check the `read_csv` documentation: https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html 

> Note: The `read_csv` function returns something called a `DataFrame`; we will be referring to it as a variable from now on.
