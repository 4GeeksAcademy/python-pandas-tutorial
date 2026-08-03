<!-- hide -->
<div align="center">

# Tutorial de Pandas: Interactivo, auto-corregido y con mentor de inteligencia artificial

[![Certificado por 4Geeks](https://img.shields.io/badge/4Geeks-certificado-2563eb?style=flat-square)](https://github.com/4GeeksAcademy/python-pandas-tutorial)
[![Autocorregido con LearnPack](https://img.shields.io/badge/LearnPack-autocorregido-2563eb?style=flat-square)](https://github.com/learnpack/learnpack)
[![Abrir en Codespaces](https://img.shields.io/badge/Abrir%20en-Codespaces-fb5a1f?style=flat-square&logo=github)](https://github.com/codespaces/new/?repo=4GeeksAcademy/python-pandas-tutorial)

</div>

🇪🇸 Español &nbsp;·&nbsp; [🇬🇧 English](https://github.com/4GeeksAcademy/python-pandas-tutorial/blob/HEAD/README.md)
<!-- endhide -->

Este tutorial interactivo de Pandas trae 22 ejercicios, 18 de ellos corregidos automáticamente con pytest, que resuelves dentro de un único archivo `app.py`. Practicas Series, `date_range`, `apply`, DataFrames, `iloc`, `loc`, `head`, `tail`, filtrado de columnas, `del`, `value_counts` y `groupby` sobre dos datasets CSV reales incluidos en el repositorio: 800 Pokémon y 1.016.395 registros de nombres de bebés en EE. UU. Nivel principiante, unas 3 horas.

<!-- hide -->
## 📋 Sobre este tutorial

- **Dificultad:** principiante
- **Duración estimada:** 3 horas
- **Ejercicios:** 22 pasos, 18 con tests automáticos
- **Tecnologías:** pandas, Python 3.10, pytest 6.2.5
- **Corrección:** incremental — LearnPack ejecuta los tests del paso actual sobre tu `app.py`
- **Idiomas de las instrucciones:** español e inglés (cada ejercicio tiene `README.es.md` y `README.md`)
- **Datasets incluidos:** `pokemon_data.csv` (800 filas, 12 columnas) y `us_baby_names_right.csv` (1.016.395 filas)
<!-- endhide -->

## 🎯 ¿Qué vas a aprender?

Pandas es la biblioteca que convierte un CSV en bruto en algo a lo que de verdad puedes hacerle preguntas. Este tutorial te lleva desde una terminal vacía hasta agregaciones agrupadas sobre un millón de filas, en cinco bloques:

- **Entorno.** Por qué conviene aislar cada proyecto, cómo crear el entorno con `pipenv shell` e instalar pandas dentro de él en lugar de ensuciar tu Python global.
- **Series.** La estructura de una dimensión: crear una `pd.Series` a partir de una lista de Python, generar un rango de fechas con `pd.date_range` y transformar todos los valores de golpe con `Series.apply`.
- **DataFrames.** La tabla de dos dimensiones: construir uno desde una lista de listas, construirlo desde una lista de diccionarios y cargarlo desde disco con `pd.read_csv`.
- **Leer y filtrar.** Asomarte a los datos con `head` y `tail`, llegar a una celda concreta con `iloc`, seleccionar columnas y rangos de filas con corchetes y filtrar filas con condiciones lógicas dentro de `loc`.
- **Limpieza.** Eliminar una columna índice sobrante con `del`, contar cuántas veces aparece cada categoría con `value_counts` y agrupar filas con `groupby(...).sum()`.

![Diagrama que muestra dos Series de pandas, una llamada apples con los valores 3, 2, 0 y 1 y otra llamada oranges con los valores 0, 3, 7 y 2, combinándose en un único DataFrame con ambas columnas juntas y un índice compartido del 0 al 3](https://raw.githubusercontent.com/4GeeksAcademy/python-pandas-tutorial/main/.learn/assets/series_dataframe.png)

Al terminar puedes responder preguntas como "¿cuántos Pokémon son legendarios?" o "¿cuántos nombres distintos hay en un dataset de un millón de filas?" con dos o tres líneas de código.

## 👀 ¿Qué vas a construir?

Aquí no hay un proyecto final de juguete: escribes código real de pandas desde el segundo ejercicio, siempre en el mismo archivo `app.py` en la raíz del repositorio. Estos son los 22 pasos, en orden:

- **Puesta a punto** — `00 Welcome`, `01 New Terminal`, `01.2 Pipenv`, `02 Install`. El motor del tutorial ocupa la primera terminal, así que abres una segunda, entras al entorno aislado con `pipenv shell` e instalas la biblioteca con `pipenv install pandas`. Ese paso se corrige buscando `pandas` dentro del `Pipfile.lock`.
- **Tu primer script** — `02.1 Create a Script`, `02.2 Import`. Creas `app.py`, imprimes `Hello World` y después haces `import pandas as pd`, cargas `.learn/assets/pokemon_data.csv` en una variable llamada `data_frame` y la imprimes.
- **Datasets** — `03 Datasets`. Abres el CSV de Pokémon incluido y lo lees como humano: 800 filas, una por Pokémon, con columnas de nombre, sus dos tipos, HP, ataque, defensa, ataque especial, defensa especial, velocidad, generación y si es legendario.
- **Series** — `04 Series`, `04.1 Date Range`, `04.2 Series Apply`. Conviertes una lista de diez edades en una Series, generas los doce días que van del `2021-05-01` al `2021-05-12` y divides entre dos todos los elementos de una Series con `apply`.
- **DataFrames desde cero** — `05 DataFrames`, `05.1 DataFrame Dict`. Montas una tabla de coches con las columnas `Brand`, `Model` y `Color` a partir de una lista bidimensional, y luego la rehaces desde una lista de diccionarios añadiendo una cuarta fila para un Tesla Model S rojo.
- **Explorar el dataset de Pokémon** — `05.2 DataFrame iLoc`, `05.3 DataFrame Head`, `05.4 DataFrame Tail`, `05.5 Print Columns`, `05.6 Loc Function`, `05.7 Filter and Count`. Imprimes una celda concreta por posición, las tres primeras filas, las tres últimas, las columnas `Name` y `Type 1` de los diez primeros Pokémon, todos los que tienen un ataque superior a 80 y, por último, cuentas cuántos legendarios hay.
- **Limpiar un millón de filas** — `06 Clean Datasets`, `06.1 Remove Column`, `06.2 Value Counts`, `06.3 Group By`. Cargas `us_baby_names_right.csv` (1.016.395 registros de nacimientos en EE. UU. con nombre, año, género, estado y cantidad), imprimes sus cinco primeras filas, borras la columna índice sin nombre que sobra, comparas cuántos registros femeninos y masculinos hay y cuentas cuántos nombres diferentes contiene.

## 🎓 ¿Qué necesitas antes de empezar?

- **Python básico.** Con variables, listas, diccionarios, `print()` y saber ejecutar un archivo con `python app.py` te sobra. Si las listas y los bucles todavía se te resisten, pasa antes por [Aprende listas y bucles de Python](https://4geeks.com/es/interactive-exercise/python-loops-lists-exercises-es).
- **Nada de matemáticas, estadística ni machine learning.** Todos los ejercicios se resuelven con funciones de pandas, no con fórmulas.
- **Una cuenta de GitHub** si quieres trabajar en la nube. El entorno preparado ya trae Python 3.10, pipenv, pytest y pandas, así que no tienes que instalar nada en tu ordenador.
- **Unas 3 horas** y una terminal que puedas dejar abierta.

## ✅ ¿Cómo funciona la corrección automática?

18 de los 22 pasos incluyen un `test.py` junto a sus instrucciones, y la corrección es incremental: al pulsar el botón de test, LearnPack ejecuta solo los tests del ejercicio en el que estás. Esos tests comprueban tres cosas distintas.

- **El código fuente de tu archivo.** La mayoría abre `app.py` como texto y busca piezas concretas: la expresión regular `import\s*pandas\s*as\s*pd`, una llamada a `print(` y, según el ejercicio, las palabras `loc`, `del`, `head`, `groupby`, `sum`, `len` o la ruta exacta del dataset `.learn/assets/pokemon_data.csv`.
- **La salida de la terminal.** Tu script se ejecuta y se captura su salida estándar para compararla con el bloque esperado carácter a carácter, alineación de columnas incluida. Por eso los enunciados te dicen exactamente cuántas filas imprimir.
- **Que no hayas hecho trampa.** `04.1`, `05.2`, `05.7` y `06.3` añaden un test antitrampas: `05.2`, `05.7` y `06.3` exigen al menos un `print(` cuyo argumento no empiece por un dígito, y `04.1` rechaza el texto `DatetimeIndex(` en cualquier parte del archivo. Pegar el resultado esperado hace fallar el ejercicio aunque la salida parezca perfecta.

17 ejercicios incluyen además un `solution.hide.py` oculto, para que compares tu solución con la de referencia cuando ya hayas aprobado.

## 💡 ¿Qué errores deberías evitar?

1. **Importar pandas de cualquier otra forma.** Casi todos los tests aplican la expresión regular `import\s*pandas\s*as\s*pd` sobre tu archivo, así que `import pandas` o `from pandas import read_csv` fallan aunque la salida sea correcta.
2. **Trabajar fuera de la raíz del repositorio.** Los datasets se referencian como `.learn/assets/...`, una ruta relativa a la raíz del proyecto, así que `app.py` tiene que estar junto a `learn.json` y ejecutarse desde ahí.
3. **Devolver en lugar de imprimir.** La corrección captura la salida estándar, o sea que todo resultado tiene que pasar por `print()`. Un valor que solo se guarda en una variable cuenta como si no hubieras impreso nada.
4. **Escribir a mano la respuesta esperada.** Un archivo cuya única salida sea `print(65)` falla en `05.7`, porque el test exige al menos un `print(` que no vaya seguido directamente de un dígito — la misma comprobación se ejecuta en `05.2` y `06.3`. Y `04.1` falla si el texto `DatetimeIndex(` aparece en cualquier parte de tu código.
5. **Imprimir un número de filas distinto.** `05.3` y `05.4` esperan exactamente tres filas, `05.5` espera los diez primeros elementos y `06` y `06.1` esperan cinco. Cualquier otro corte genera otro bloque de salida y no pasa.
6. **Olvidar `pipenv shell`.** El entorno no es permanente: cada vez que abras una terminal nueva tienes que volver a entrar, o parecerá que pandas no está instalado.
7. **Empezar un script nuevo en cada ejercicio.** A partir de `05.3` varios enunciados dicen "usa la misma variable DataFrame del ejercicio anterior": sigues editando el mismo `app.py`.

## ❓ Preguntas frecuentes

### ¿Necesito saber machine learning para hacer este tutorial de Pandas?

No. Solo se da por supuesto Python básico. Pandas es el paso de manejo de datos que va *antes* de cualquier modelo: cargas un CSV, lo miras, lo filtras y lo limpias. Aquí no se entrena ningún modelo ni hace falta estadística.

### ¿Puedo hacer los ejercicios sin instalar Python en mi ordenador?

Sí. El repositorio incluye una configuración de dev container con Python 3.10, Node.js 22 y el motor del tutorial ya instalados, así que abrirlo en un entorno en la nube como GitHub Codespaces te da una terminal lista en un par de minutos. Instalarlo en local es opcional y está documentado en el repositorio.

### ¿Cuál es la diferencia entre una Series y un DataFrame?

Una Series es unidimensional, como una lista etiquetada: `pd.Series([23, 45, 7])` te da los valores con un índice al lado. Un DataFrame es bidimensional, como una tabla o una hoja de cálculo, y cada una de sus columnas es en realidad una Series. Los ejercicios `04` a `04.2` cubren las Series; a partir del `05` todo son DataFrames.

### ¿Por qué falla mi ejercicio si la salida de la terminal parece correcta?

Porque la comparación es literal. Los tests buscan el texto esperado dentro de tu salida estándar, así que una columna de menos, un número de filas distinto o un valor impreso con otro tipo ya provocan que no coincida. Lee el bloque de resultado esperado del enunciado y reprodúcelo tal cual, incluidas las filas que imprimes.

### ¿Qué datasets vienen incluidos?

Dos, ambos dentro de `.learn/assets/`. `pokemon_data.csv` tiene 800 filas y 12 columnas y se usa desde el ejercicio `02.2` hasta el `05.7`. `us_baby_names_right.csv` contiene 1.016.395 registros de nacimientos en EE. UU. sacados de un [dataset conocido de Kaggle](https://www.kaggle.com/kaggle/us-baby-names) y se usa en todo el bloque `06` de limpieza.

### ¿Puedo usar Jupyter Notebook o Google Colab en lugar de app.py?

Puedes experimentar donde quieras, pero la corrección solo lee el `app.py` de la raíz del proyecto y la salida estándar que produce al ejecutarse, así que para aprobar los tests tu código final tiene que acabar en ese archivo.

<!-- hide -->
## 📝 Tutoriales relacionados

- [Aprende Python Interactivamente (principiante)](https://4geeks.com/es/interactive-exercise/python-beginner-exercises-es)
- [Aprende listas y bucles de Python Interactivamente](https://4geeks.com/es/interactive-exercise/python-loops-lists-exercises-es)
- [Aprende las funciones de Python Interactivamente](https://4geeks.com/es/interactive-exercise/python-function-exercises-es)
- [Domina Python Practicando](https://4geeks.com/es/interactive-exercise/master-python-exercises-es)
- [Aprende Programación Orientada a Objetos con Python](https://4geeks.com/es/interactive-exercise/aprende-programacion-orientada-a-objetos-con-python)
- [Aprende las Mejores Prácticas de Python](https://4geeks.com/es/interactive-exercise/aprende-las-mejores-practicas-de-python)

## 🚀 Cómo empezar

El camino más rápido es el lanzador de un clic, que te prepara todo el entorno en la nube:

1. Abre el [lanzador de un clic](https://s.4geeks.com/start?repo=https://github.com/4GeeksAcademy/python-pandas-tutorial&lang=es&utm_source=github&utm_medium=organic&utm_content=readme) y elige dónde quieres ejecutar el tutorial.

2. Espera a que se construya el contenedor. Instala Python 3.10, Node.js 22, pandas, pytest y el motor del tutorial.

3. Abre una terminal **nueva** (menú → Terminal → New Terminal), porque el motor del tutorial mantiene ocupada la primera.

4. Sigue las instrucciones en pantalla y pulsa el botón de test en cada ejercicio.

También puedes abrir el repositorio directamente en [GitHub Codespaces](https://github.com/codespaces/new/?repo=4GeeksAcademy/python-pandas-tutorial), que usa la configuración `.devcontainer` incluida.

## 💻 Instalación local

Si prefieres trabajar en tu propia máquina, necesitas Node.js 20 o superior y Python 3.10 o superior disponibles en tu terminal.

1. Instala el motor del tutorial y su plugin de Python:

   ```bash
   npm i @learnpack/learnpack@5 -g
   learnpack plugins:install @learnpack/python
   ```

2. Clona el repositorio y entra en la carpeta:

   ```bash
   git clone https://github.com/4GeeksAcademy/python-pandas-tutorial.git
   cd python-pandas-tutorial
   ```

3. Crea el entorno e instala las dependencias que esperan los ejercicios:

   ```bash
   pipenv shell
   pipenv install pandas
   pip install pytest==6.2.5 pytest-testdox mock
   ```

4. Arranca el tutorial y abre la dirección que aparece en pantalla:

   ```bash
   learnpack start
   ```

> 💡 Recuerda que `pipenv shell` hay que volver a ejecutarlo en cada terminal nueva.

## 📚 Cómo están organizados los ejercicios

Cada paso vive en su propia carpeta dentro de [`.learn/exercises`](https://github.com/4GeeksAcademy/python-pandas-tutorial/tree/HEAD/.learn/exercises), numerada para fijar su posición en el tutorial:

- `README.es.md` y `README.md`: las instrucciones, en español e inglés.
- `test.py`: el archivo de pytest que corrige el paso, presente en 18 de las 22 carpetas.
- `solution.hide.py`: la solución de referencia, presente en 17 carpetas y oculta hasta que terminas.

Los datasets y las capturas que usan los enunciados están en `.learn/assets/`, y los metadatos del tutorial (título, descripción, dificultad, duración y modo de corrección) están en [`learn.json`](https://github.com/4GeeksAcademy/python-pandas-tutorial/blob/HEAD/learn.json). Tu código siempre va en un único archivo `app.py` en la raíz del proyecto.

## 🤝 Colaboradores

Gracias a las personas que crearon y revisaron estos ejercicios:

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

Puedes ver la lista completa en el [gráfico de colaboradores](https://github.com/4GeeksAcademy/python-pandas-tutorial/graphs/contributors). Este tutorial forma parte de los ejercicios interactivos que mantiene [4Geeks Academy](https://4geeksacademy.com/us/coding-bootcamps/datascience-machine-learning) y funciona con [LearnPack](https://4geeks.com/es/learnpack) y el mentor de IA [Rigobot](https://4geeks.com/es/rigobot). ¿Has encontrado un error o quieres añadir un ejercicio? Abre un [issue](https://github.com/4GeeksAcademy/python-pandas-tutorial/issues) o una pull request.
<!-- endhide -->
