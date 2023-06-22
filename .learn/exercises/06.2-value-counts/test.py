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

@pytest.mark.it("Use the value_counts function")
def test_value_counts_exist():
    f = open('app.py')
    content = f.read()
    assert "value_counts" in content

@pytest.mark.it("You should be reading the csv file located at .learn/assets/us_baby_names_right.csv to create your DataFrame")
def test_reading_csv():
    f = open('app.py')
    content = f.read()
    assert ".learn/assets/us_baby_names_right.csv" in content and 'read_csv' in content

@pytest.mark.it('The output should be the expected')
def test_expected_output(capsys):
    import app
    captured = capsys.readouterr()
    assert captured.out == """Gender
F    558846
M    457549
Name: count, dtype: int64
"""
