# Using  loc function in Pandas

You can also use the `data_frame.loc` function to filter records using logical operations as indexes, like this:

```python
# get people more than 18 years old
data_frame.loc[data_frame['age'] < 18]
```

## 📝 Instructions:

1. Using the `loc` function, print on the terminal all pokemons with an atack of more than 80.

## Expected Result:

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