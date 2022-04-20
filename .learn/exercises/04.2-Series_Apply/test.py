import io, os, re, sys, pytest

@pytest.mark.it('You must import pandas')
def test_import_pandas():
    path = os.path.dirname(os.path.abspath('app.py'))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"import\s*pandas")
        assert bool(regex.search(content)) == True

@pytest.mark.it("Use the print function")
def test_output():
    f = open(os.path.dirname(os.path.abspath('app.py')) + '/app.py')
    content = f.read()
    assert content.find("print(") > 0

@pytest.mark.it('The variable my_series should exist')
def test_variable_existence():
    from app import my_series

@pytest.mark.it('The output should be the expected')
def test_expected_output(capsys):
    import app
    captured = capsys.readouterr()
    assert captured.out == """0    1.0
1    2.0
2    3.0
3    4.0
4    5.0
dtype: float64"""