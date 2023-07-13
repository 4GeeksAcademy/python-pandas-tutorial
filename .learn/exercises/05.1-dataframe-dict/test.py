import pytest, io, os, sys, re

@pytest.mark.it('You must import pandas')
def test_import_pandas():
    path = 'app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"import\s*pandas\s*as\s*pd")
        assert bool(regex.search(content)) == True

@pytest.mark.it("Use the print function")
def test_output():
    path = os.path.dirname(os.path.abspath('app.py'))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"print\s*\(")
        assert bool(regex.search(content)) == True

@pytest.mark.it('You should not be using list, use dict instead to create DataFrame')
def test_list_in_file():
    path = 'app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        # if the user uses this, then they are most likely using a list instead of dict to create DataFrame
        pattern = r'columns\s*=\s*'
        regex = re.compile(pattern)
        assert bool(regex.search(content)) == False



@pytest.mark.it('The output should be the expected')
def test_expected_output(capsys):
    import app
    captured = capsys.readouterr()
    assert   """    brand     make   color
0  Toyota  Corolla    Blue
1    Ford        K  Yellow
2  Porche  Cayenne   White
3   Tesla  Model S     Red
""" in captured.out
