# `05.6` Loc Function 

Puedes usar la función `loc` para filtrar registros usando operaciones lógicas como índices, así:

```python
# Conseguir personas mayores de 18 años
data_frame.loc[data_frame['age'] > 18]
```

## 📝 Instrucciones:

1. Usa la misma variable de DataFrame que usaste en el ejercicio anterior.

2. Usando la función `loc`, imprime en el terminal todos los pokemons con un ataque de más de 80.

## 💻 Resultado Esperado: 

```bash
       #                       Name   Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary
2      3                   Venusaur    Grass  Poison  80      82       83      100      100     80           1      False
3      3      VenusaurMega Venusaur    Grass  Poison  80     100      123      122      120     80           1      False
6      6                  Charizard     Fire  Flying  78      84       78      109       85    100           1      False
7      6  CharizardMega Charizard X     Fire  Dragon  78     130      111      130       85    100           1      False
8      6  CharizardMega Charizard Y     Fire  Flying  78     104       78      159      115    100           1      False
..   ...                        ...      ...     ...  ..     ...      ...      ...      ...    ...         ...        ...
795  719                    Diancie     Rock   Fairy  50     100      150      100      150     50           6       True
796  719        DiancieMega Diancie     Rock   Fairy  50     160      110      160      110    110           6       True
797  720        HoopaHoopa Confined  Psychic   Ghost  80     110       60      150      130     70           6       True
798  720         HoopaHoopa Unbound  Psychic    Dark  80     160       60      170      130     80           6       True
799  721                  Volcanion     Fire   Water  80     110      120      130       90     70           6       True
```
