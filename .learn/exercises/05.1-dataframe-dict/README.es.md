# `05.1` DataFrame Dict

Otra manera de organizar tus datos antes de crear un DataFrame será usando `dict` (diccionario) en vez de `list`.

En este ejemplo tenemos una lista de diccionarios que hace más fácil la lectura de los datos antes de crear el DataFrame.

```python
data = [
    { 
        "brand": "Toyota", 
        "model": "Corolla",
        "color": "Blue"
    },
    {
        "brand": "Ford", 
        "model": "K",
        "color": "Yellow"
    },
    {
        "brand": "Porsche", 
        "model": "Cayenne",
        "color": "White"
    }
]
```

## 📝 Instrucciones: 

1. Usa estos datos para crear un DataFrame pero agrégale una nueva fila para un Tesla, Model S, Red. 

## 💻 Resultado Esperado:

```bash
     brand    model   color
0   Toyota  Corolla    Blue
1     Ford        K  Yellow
2  Porsche  Cayenne   White
3    Tesla  Model S     Red
```
