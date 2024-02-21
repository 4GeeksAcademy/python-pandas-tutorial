# `02.2` Import 

Ahora, vamos a añadir Pandas en nuestro script utilizando el comando `import`. 

El comando `import` está destinado para cargar librerías de terceros (como Pandas) u otros archivos de Python que hayas creado (que haremos en el futuro).

## 📝 Instrucciones:

1. Escribe `import pandas as pd` dentro del archivo `app.py` para importar la librería de Pandas.

2. Crea una variable llamada `data_frame`.

3. Utiliza la función de Pandas `read_csv` para importar el contenido del archivo CSV en esta ruta `.learn/assets/pokemon_data.csv` y asígnalo a la variable `data_frame`

4. Imprime la variable en el terminal usando la función `print`.

## 💻 Resultado Esperado:

Corre tu script y deberías ver la siguiente salida:

![correr archivo app.py](../../assets/print-file.png)

## 💡 Pista:

+ Echa un vistazo a la documentación de `read_csv`: https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html

> Nota: La función `read_csv` devuelve algo llamado `DataFrame`; nos estaremos refiriendo a eso como una variable de ahora en adelante.
