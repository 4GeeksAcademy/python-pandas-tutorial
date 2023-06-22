import io, os, re, sys, pytest, pandas

@pytest.mark.it('You must import pandas')
def test_import_pandas():
    path = 'app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"import\s*pandas\s*as\s*pd")
        assert bool(regex.search(content)) == True

@pytest.mark.it("Use the print function")
def test_output():
    f = open('app.py')
    content = f.read()
    assert "print" in content

@pytest.mark.it("Use the tail function")
def test_output():
    f = open('app.py')
    content = f.read()
    assert "tail" in content


@pytest.mark.it('The output should be the expected')
def test_expected_output(capsys):
    import app
    captured = capsys.readouterr()
    data_frame = pandas.read_csv('.learn/assets/pokemon_data.csv').tail(3)
    assert captured.out == str(data_frame)+'\n'

@pytest.mark.it("You should be reading the csv file located at .learn/assets/pokemon_data.csv to create your DataFrame")
def test_reading_csv():
    f = open('app.py')
    content = f.read()
    assert ".learn/assets/pokemon_data.csv" in content and 'read_csv' in content