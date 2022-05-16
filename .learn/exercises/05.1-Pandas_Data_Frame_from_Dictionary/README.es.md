# Pandas Data Frame from Dictionary

Otra manera de organizar tus datos antes de crear un DataFrame será usando `dict` en vez de `list`.

En este ejemplo tenemos una lista de `dicts` que hace más fácil la lectura de los datos antes de crear el DataFrame.


```python
data = [
    { 
        "brand": "Toyota", 
        "make": "Corolla",
        "color": "Blue"
    },
    {
        "brand": "Ford", 
        "make": "K",
        "color": "Yellow"
    },
    {
        "brand": "Porche", 
        "make": "Cayenne",
        "color": "White"
    }
]
```

## 📝 Instrucciones: 

1. Usa estos datos para crear un DataFrame pero agrégale una nueva fila para un Tesla modelo S rojo. 

## Resultado Esperado:

```bash
    Brand     Make   Color
0  Toyota  Corolla    Blue
1    Ford        K  Yellow
2  Porche  Cayenne   White
3  Tesla   Model S     Red
```