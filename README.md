<!-- hide -->
<div align="center">

# Pandas tutorial exercises

[![Certified by 4Geeks](https://img.shields.io/badge/4Geeks-certified-2563eb?style=flat-square)](https://github.com/4GeeksAcademy/python-pandas-tutorial)
[![LearnPack autograded](https://img.shields.io/badge/LearnPack-autograded-2563eb?style=flat-square)](https://github.com/learnpack/learnpack)
[![Open in Codespaces](https://img.shields.io/badge/Open%20in-Codespaces-fb5a1f?style=flat-square&logo=github)](https://github.com/codespaces/new/?repo=4GeeksAcademy/python-pandas-tutorial)

</div>

🇬🇧 English &nbsp;·&nbsp; [🇪🇸 Español](https://github.com/4GeeksAcademy/python-pandas-tutorial/blob/HEAD/README.es.md)
<!-- endhide -->

This interactive Pandas tutorial ships 22 exercises, 18 of them graded automatically by pytest, that you solve inside a single `app.py` file. You practice Series, `date_range`, `apply`, DataFrames, `iloc`, `loc`, `head`, `tail`, column filtering, `del`, `value_counts` and `groupby` on two real CSV datasets included in the repository: 800 Pokémon and 1,016,395 US baby-name records. Beginner level, around 3 hours.

<!-- hide -->
## 📋 About this tutorial

- **Difficulty:** beginner
- **Estimated duration:** 3 hours
- **Exercises:** 22 steps, 18 with automated tests
- **Technologies:** pandas, Python 3.10, pytest 6.2.5
- **Grading:** incremental — LearnPack runs the tests of the current step against your `app.py`
- **Instruction languages:** English and Spanish (every exercise has `README.md` and `README.es.md`)
- **Datasets included:** `pokemon_data.csv` (800 rows, 12 columns) and `us_baby_names_right.csv` (1,016,395 rows)
<!-- endhide -->

## 🎯 What will you learn?

Pandas is the library that turns a raw CSV file into something you can actually ask questions to. This tutorial takes you from an empty terminal to grouped aggregations over a million rows, in five blocks:

- **Environment.** Why an isolated environment matters, how to create one with `pipenv shell`, and how to install pandas inside it instead of polluting your global Python.
- **Series.** The one-dimensional structure: build a `pd.Series` from a Python list, generate a range of dates with `pd.date_range`, and transform every value at once with `Series.apply`.
- **DataFrames.** The two-dimensional table: create one from a list of lists, create one from a list of dictionaries, and load one from disk with `pd.read_csv`.
- **Reading and filtering.** Inspect data with `head` and `tail`, reach a single cell with `iloc`, select columns and row ranges with square brackets, and filter rows with boolean conditions inside `loc`.
- **Cleaning.** Drop a leftover index column with `del`, count how often each category appears with `value_counts`, and aggregate rows with `groupby(...).sum()`.

![Diagram showing two pandas Series, one labelled apples with the values 3, 2, 0, 1 and another labelled oranges with the values 0, 3, 7, 2, being combined into a single DataFrame with both columns side by side and a shared index from 0 to 3](https://raw.githubusercontent.com/4GeeksAcademy/python-pandas-tutorial/main/.learn/assets/series_dataframe.png)

By the end you can answer questions such as "how many Pokémon are legendary?" or "how many distinct baby names appear in a million-row dataset?" in two or three lines of code.

## 👀 What will you build?

There is no toy project at the end: you write real pandas code from the second exercise onward, always in the same `app.py` file at the root of the repository. These are the 22 steps, in order:

- **Getting set up** — `00 Welcome`, `01 New Terminal`, `01.2 Pipenv`, `02 Install`. The tutorial engine takes over the first terminal, so you open a second one, run `pipenv shell` to enter an isolated environment, and install the library with `pipenv install pandas`. The install step is graded by looking for `pandas` inside `Pipfile.lock`.
- **Your first script** — `02.1 Create a Script`, `02.2 Import`. Create `app.py`, print `Hello World`, then `import pandas as pd`, load `.learn/assets/pokemon_data.csv` into a variable called `data_frame` and print it.
- **Datasets** — `03 Datasets`. Open the included Pokémon CSV and read it as a human: 800 rows, one per Pokémon, with columns for name, both types, HP, attack, defense, special attack, special defense, speed, generation and whether it is legendary.
- **Series** — `04 Series`, `04.1 Date Range`, `04.2 Series Apply`. Turn a list of ten ages into a Series, generate the twelve days between `2021-05-01` and `2021-05-12`, and divide every element of a Series by two with `apply`.
- **DataFrames from scratch** — `05 DataFrames`, `05.1 DataFrame Dict`. Build a car table with the columns `Brand`, `Model` and `Color` from a two-dimensional list, then rebuild it from a list of dictionaries and add a fourth row for a red Tesla Model S.
- **Exploring the Pokémon dataset** — `05.2 DataFrame iLoc`, `05.3 DataFrame Head`, `05.4 DataFrame Tail`, `05.5 Print Columns`, `05.6 Loc Function`, `05.7 Filter and Count`. Print one single cell by position, the first three rows, the last three rows, the `Name` and `Type 1` columns for the first ten Pokémon, every Pokémon with an attack above 80, and finally count how many legendary Pokémon exist.
- **Cleaning a million rows** — `06 Clean Datasets`, `06.1 Remove Column`, `06.2 Value Counts`, `06.3 Group By`. Load `us_baby_names_right.csv` (1,016,395 US birth records with name, year, gender, state and count), print its first five rows, delete the unnamed leftover index column, compare how many female and male records it holds, and count how many different names it contains.

## 🎓 What do you need before starting?

- **Basic Python.** Variables, lists, dictionaries, `print()` and running a file with `python app.py` is enough. If lists and loops still feel unfamiliar, do [Learn Python Loops and lists](https://4geeks.com/en/interactive-exercise/python-loops-lists-exercises) first.
- **No maths, statistics or machine-learning background.** Every exercise is solved with pandas functions, not with formulas.
- **A GitHub account** if you want to run everything in the cloud. The prepared environment already includes Python 3.10, pipenv, pytest and pandas, so there is nothing to install on your computer.
- **Around 3 hours** and a terminal you are willing to keep open.

## ✅ How does the automatic grading work?

18 of the 22 steps ship a `test.py` next to their instructions, and grading is incremental: when you press the test button, LearnPack runs only the tests of the exercise you are on. Those tests check three different things.

- **The source of your file.** Most tests read `app.py` as text and look for specific pieces: the regular expression `import\s*pandas\s*as\s*pd`, a call to `print(`, and depending on the exercise the words `loc`, `del`, `head`, `groupby`, `sum`, `len` or the exact dataset path `.learn/assets/pokemon_data.csv`.
- **The terminal output.** Your script is executed and its standard output is captured, then compared against the expected block character by character, column alignment included. This is why the exercises tell you exactly how many rows to print.
- **That you did not cheat.** `04.1`, `05.2`, `05.7` and `06.3` add an anti-hardcoding test: `05.2`, `05.7` and `06.3` require at least one `print(` whose argument does not start with a digit, and `04.1` rejects the text `DatetimeIndex(` anywhere in your file. Pasting the expected result fails even though the output would look perfect.

17 exercises also include a hidden `solution.hide.py`, so you can compare your approach with the reference one after you pass.

## 💡 What mistakes should you avoid?

1. **Importing pandas any other way.** Nearly every test runs the regular expression `import\s*pandas\s*as\s*pd` over your file, so `import pandas` or `from pandas import read_csv` fails even when the output is correct.
2. **Working outside the repository root.** The datasets are referenced as `.learn/assets/...`, a path relative to the project root, so `app.py` must sit next to `learn.json` and be executed from there.
3. **Returning instead of printing.** Grading captures standard output, so every result has to go through `print()`. A value that is only stored in a variable counts as no output at all.
4. **Hardcoding the expected answer.** A file whose only output is `print(65)` fails `05.7`, because the test demands at least one `print(` that is not followed directly by a digit — the same check runs in `05.2` and `06.3`. And `04.1` fails if the text `DatetimeIndex(` appears anywhere in your code.
5. **Printing the wrong number of rows.** `05.3` and `05.4` expect exactly three rows, `05.5` expects the first ten, and `06` and `06.1` expect five. Any other slice produces a different output block and fails.
6. **Forgetting `pipenv shell`.** The environment is not permanent: every time you open a new terminal you have to enter it again, or pandas will look uninstalled.
7. **Starting a new script on every exercise.** From `05.3` onward several statements say "use the same DataFrame variable you used in the previous exercise": you keep editing the same `app.py`.

## ❓ Frequently asked questions

### Do I need to know machine learning to follow this Pandas tutorial?

No. The tutorial only assumes basic Python. Pandas is the data-handling step that comes *before* any model: you load a CSV, look at it, filter it and clean it. Nothing here trains a model or requires statistics.

### Can I do the exercises without installing Python on my computer?

Yes. The repository includes a dev container configuration with Python 3.10, Node.js 22 and the tutorial engine already installed, so opening it in a cloud environment such as GitHub Codespaces gives you a working terminal in a couple of minutes. Installing locally is optional and documented in the repository.

### What is the difference between a Series and a DataFrame?

A Series is one-dimensional, like a labelled list: `pd.Series([23, 45, 7])` gives you values with an index next to them. A DataFrame is two-dimensional, like a table or a spreadsheet, and each of its columns is in fact a Series. Exercises `04` to `04.2` cover Series; from `05` onward everything is DataFrames.

### Why does my exercise fail if the terminal output looks correct?

Because the comparison is literal. The tests look for the expected text inside your standard output, so a missing column, a different number of rows or a value printed with a different type produces a mismatch. Read the expected result block in the exercise and reproduce it exactly, including how many rows you print.

### What datasets are included?

Two, both inside `.learn/assets/`. `pokemon_data.csv` has 800 rows and 12 columns and is used from exercise `02.2` to `05.7`. `us_baby_names_right.csv` holds 1,016,395 US birth records taken from a well-known [Kaggle dataset](https://www.kaggle.com/kaggle/us-baby-names) and is used in the whole `06` cleaning block.

### Can I use Jupyter Notebook or Google Colab instead?

You can experiment anywhere you like, but the grading only reads `app.py` in the project root and the standard output it produces when executed, so to pass the tests your final code has to live in that file.

<!-- hide -->
## 📝 Related tutorials

- [Learn Python Interactively (beginner)](https://4geeks.com/en/interactive-exercise/python-beginner-exercises)
- [Learn Python Loops and lists Interactively](https://4geeks.com/en/interactive-exercise/python-loops-lists-exercises)
- [Learn Python Functions Interactively](https://4geeks.com/en/interactive-exercise/python-function-exercises)
- [Master Python by practice](https://4geeks.com/en/interactive-exercise/master-python-exercises)
- [Learn Object Oriented Programming with Python](https://4geeks.com/en/interactive-exercise/object-oriented-programing-with-python)
- [Linear Algebra in Python and NumPy](https://4geeks.com/en/interactive-exercise/linear-algebra-in-python-and-numpy)

## 🚀 How to start

The fastest path is the one-click launcher, which prepares the whole environment in the cloud for you:

1. Open the [one-click launcher](https://s.4geeks.com/start?repo=https://github.com/4GeeksAcademy/python-pandas-tutorial&lang=us&utm_source=github&utm_medium=organic&utm_content=readme) and choose where you want to run the tutorial.

2. Wait for the container to build. It installs Python 3.10, Node.js 22, pandas, pytest and the tutorial engine.

3. Open a **new** terminal (menu → Terminal → New Terminal), because the tutorial engine keeps the first one busy.

4. Follow the instructions on screen and press the test button on each exercise.

You can also open the repository directly in [GitHub Codespaces](https://github.com/codespaces/new/?repo=4GeeksAcademy/python-pandas-tutorial) using the included `.devcontainer` configuration.

## 💻 Local installation

If you prefer to work on your own machine, you need Node.js 20+ and Python 3.10+ available in your terminal.

1. Install the tutorial engine and its Python plugin:

   ```bash
   npm i @learnpack/learnpack@5 -g
   learnpack plugins:install @learnpack/python
   ```

2. Clone the repository and move into it:

   ```bash
   git clone https://github.com/4GeeksAcademy/python-pandas-tutorial.git
   cd python-pandas-tutorial
   ```

3. Create the environment and install the dependencies the exercises expect:

   ```bash
   pipenv shell
   pipenv install pandas
   pip install pytest==6.2.5 pytest-testdox mock
   ```

4. Start the tutorial and open the address it prints:

   ```bash
   learnpack start
   ```

> 💡 Remember that `pipenv shell` has to be run again in every new terminal session.

## 📚 How the exercises are organized

Each step lives in its own folder under [`.learn/exercises`](https://github.com/4GeeksAcademy/python-pandas-tutorial/tree/HEAD/.learn/exercises), named with the number that fixes its position in the tutorial:

- `README.md` and `README.es.md`: the instructions, in English and Spanish.
- `test.py`: the pytest file that grades the step, present in 18 of the 22 folders.
- `solution.hide.py`: the reference solution, present in 17 folders and hidden until you finish.

The datasets and the screenshots used by the instructions are in `.learn/assets/`, and the tutorial metadata (title, description, difficulty, duration and grading mode) is in [`learn.json`](https://github.com/4GeeksAcademy/python-pandas-tutorial/blob/HEAD/learn.json). Your own code always goes in a single `app.py` file at the root of the project.

## 🤝 Contributors

Thanks to the people who built and reviewed these exercises:

- Jose Mora — [@josemoracard](https://github.com/josemoracard)
- Alejandro Sanchez — [@alesanchezr](https://github.com/alesanchezr)
- Charly Chacón — [@Charlytoc](https://github.com/Charlytoc)
- Tomas Gonzalez — [@tommygonzaleza](https://github.com/tommygonzaleza)
- Martín Suárez — [@kiddopro](https://github.com/kiddopro)
- Lorena Gubaira — [@Lorenagubaira](https://github.com/Lorenagubaira)
- Ehiber Graterol — [@ehiber](https://github.com/ehiber)
- Jennifer Toledo — [@jatv93](https://github.com/jatv93)
- Ernesto Gonzalez — [@UmiKami](https://github.com/UmiKami)
- Rodolfo Pacheco — [@rvpacheco](https://github.com/rvpacheco)
- Hernán García — [@hernanjkd](https://github.com/hernanjkd)
- Deimian Vásquez — [@deimianvasquez](https://github.com/deimianvasquez)

You can see the full list in the [contributors graph](https://github.com/4GeeksAcademy/python-pandas-tutorial/graphs/contributors). This tutorial is part of the interactive exercises maintained by [4Geeks Academy](https://4geeksacademy.com/us/coding-bootcamps/datascience-machine-learning) and is powered by [LearnPack](https://4geeks.com/en/learnpack) and the [Rigobot](https://4geeks.com/en/rigobot) AI mentor. Found a mistake or want to add an exercise? Open an [issue](https://github.com/4GeeksAcademy/python-pandas-tutorial/issues) or a pull request.
<!-- endhide -->
