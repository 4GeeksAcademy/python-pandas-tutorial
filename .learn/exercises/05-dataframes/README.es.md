# `05` DataFrames

Los DataFrames (marco de datos) son un concepto similar a las "tablas" o "datos tabulados". Puedes crear un DataFrame a partir cualquier Dataset.

![Ejemplo de DataFrame](../../assets/dataframe.jpeg)

Puedes crear manualmente un DataFrame de una lista de Python con el siguiente código:

```python
import pandas as pd
# Array bidimensional con valores [name, age]
data = [['Alex', 10], ['Bob', 12], ['Clarke', 13]]

# Crea un DataFrame y nombra las columnas
df = pd.DataFrame(data, columns=['Name', 'Age'])

# Imprime el DataFrame
print(df)
```

## 📝 Instrucciones:

1. Por favor crea e imprime un DataFrame con los siguientes datos. Las etiquetas de las columnas serán: `Brand, Model, Color`.

```python
data = [["Toyota", "Corolla", "Blue"], ["Ford", "K", "Yellow"], ["Porsche", "Cayenne", "White"]]
```

## 💻 Resultado Esperado:

Corre tu código en el terminal y la salida debería ser similar a esta:

```bash
     Brand    Model   Color
0   Toyota  Corolla    Blue
1     Ford        K  Yellow
2  Porsche  Cayenne   White
```
