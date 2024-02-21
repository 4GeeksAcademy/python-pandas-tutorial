# `05.2` DataFrame iLoc

El comando `iloc` te permite recuperar cualquier celda en tu DataFrame. Por ejemplo, para imprimir la celda en el `x-axis:2` y `y-axis:4` tendríamos que escribir lo siguiente:

```python
# Imprimir el elemento en la Fila: 2, Columna: 4
# Recuerda que el índice comienza en 0

print(data_frame.iloc[2,4])
```

## 📝 Instrucciones:

1. Crea un DataFrame utilizando el archivo `.csv` ubicado en `.learn/assets/pokemon_data.csv`

2. Imprime la fila 133, columna 6 del DataFrame en el terminal.

## 💻 Resultado Esperado:

La salida en el terminal debería ser `35`.
