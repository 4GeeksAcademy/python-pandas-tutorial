import io, os, sys, pytest, re


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

@pytest.mark.it('The output should be the expected')
def test_expected_output(capsys):
    import app
    captured = capsys.readouterr()
    assert "65\n" in captured.out

@pytest.mark.it("Do not hardcode the expected output")
def test_harcoded_output():
    path = os.path.dirname(os.path.abspath('app.py'))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"print\s*\((?!\s*\d)")
        assert bool(regex.search(content)) == True

@pytest.mark.it("Use the loc function")
def test_loc_func_exists():
    f = open('app.py')
    content = f.read()
    assert "loc" in content

@pytest.mark.it("You should be reading the csv file located at .learn/assets/pokemon_data.csv to create your DataFrame")
def test_reading_csv():
    f = open('app.py')
    content = f.read()
    assert ".learn/assets/pokemon_data.csv" in content and 'read_csv' in content