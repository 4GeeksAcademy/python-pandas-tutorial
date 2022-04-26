import pytest, io, os, sys, re, pandas
data_frame = pandas.read_csv('.learn/assets/pokemon_data.csv').head(3)

@pytest.mark.it('You must import pandas')
def test_import_pandas():
    path = os.path.dirname(os.path.abspath('app.py'))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"import\s*pandas\s*as\s*pd")
        assert bool(regex.search(content)) == True

@pytest.mark.it("Use the print function")
def test_output():
    f = open('app.py')
    content = f.read()
    assert "print" in content


@pytest.mark.it('The output should be the expected')
def test_expected_output(capsys):
    import app
    captured = capsys.readouterr()
    assert captured.out == str(data_frame) + '\n'

# @pytest.mark.it('The variable data_frame should exist')
# def test_variable_existence():
#     from app import data_frame

"""
   #       Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary
0  1  Bulbasaur  Grass  Poison  45      49       49       65       65     45           1      False
1  2    Ivysaur  Grass  Poison  60      62       63       80       80     60           1      False
2  3   Venusaur  Grass  Poison  80      82       83      100      100     80           1      False
"""