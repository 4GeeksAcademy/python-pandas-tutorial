import io, os, sys, pytest, re

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
    assert captured.out == """                        Name Type 1
0                  Bulbasaur  Grass
1                    Ivysaur  Grass
2                   Venusaur  Grass
3      VenusaurMega Venusaur  Grass
4                 Charmander   Fire
5                 Charmeleon   Fire
6                  Charizard   Fire
7  CharizardMega Charizard X   Fire
8  CharizardMega Charizard Y   Fire
9                   Squirtle  Water
"""