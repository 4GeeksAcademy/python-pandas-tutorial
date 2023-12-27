# `05.5` Print Columns

Tu puedes imprimir solo una columna de tu elección, por ejemplo:

```python
print(data_frame['Type 1']) # Esto imprimirá solo la columna "Tipo 1"
```

También puedes utilizar los corchetes `[]` para elegir el rango de filas tu quieres imprimir, así:

```python
print(data_frame[0:10])
```

O puedes combinar ambos trucos, de esta manera:

```python
print(data_frame['Type 1'][0:10])
```

## 📝 Instrucciones:

1. Usa la misma variable de DataFrame que usaste en el ejercicio anterior.
2. Imprime solamente las columnas  'Name' y 'Type 1' desde tu Dataset, y solo los primeros 10 elementos.

## Resultado Esperado:

Tu terminal se debería ver así:

![print file](../../assets/07-print-columns.png)

