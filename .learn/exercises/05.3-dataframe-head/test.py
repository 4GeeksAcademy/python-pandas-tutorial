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

@pytest.mark.it("Use the head function")
def test_output():
    f = open('app.py')
    content = f.read()
    assert "head" in content
    
@pytest.mark.it("You should be reading the csv file located at .learn/assets/pokemon_data.csv to create your DataFrame")
def test_reading_csv():
    f = open('app.py')
    content = f.read()
    assert ".learn/assets/pokemon_data.csv" in content and 'read_csv' in content

@pytest.mark.it('The output should be the expected')
def test_expected_output(capsys):
    import app
    captured = capsys.readouterr()
    assert str(data_frame) + '\n' in captured.out
