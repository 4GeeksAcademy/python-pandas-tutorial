# `02.2` Import 

Ahora, vamos a añadir Pandas en nuestro script utilizando el comando `import`. 

El comando `import` está destinado para cargar librerías de terceros (como Pandas) u otros archivos de Python que hayas creado (que haremos en el futuro).

## 📝 Instrucciones:

1. Escribe `import pandas as pd` dentro del archivo `app.py` para importar la librería de Pandas.

2. Utiliza la función de Pandas `read_csv` para importar el contenido del archivo CSV en una variable llamada `data_frame`.

3. Imprime la variable en el terminal usando la función `print`.

## 💻 Resultado Esperado:

Corre tu script y deberías ver la siguiente salida:

![correr archivo app.py](../../assets/print-file.png)

## 💡 Pista:

+ Tu código debería ser algo así

```python
import pandas as pd

data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
print(data_frame)
```

> Nota: La función `read_csv` devuelve algo llamado `DataFrame`; nos estaremos refiriendo a eso como una variable de ahora en adelante.
