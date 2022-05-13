import io, os, sys, pytest, re, pandas
data = pandas.read_csv('.learn/assets/pokemon_data.csv')

@pytest.mark.it('You must import pandas')
def test_import_pandas():
    path = os.path.dirname(os.path.abspath('app.py'))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"import\s*pandas\s*as\s*pd")
        assert bool(regex.search(content)) == True

@pytest.mark.it('The variable data_frame must exist')
def test_vatiable_existence():
    from app import data_frame

@pytest.mark.it("Use the print function")
def test_output():
    f = open('app.py')
    content = f.read()
    assert "print(" in content

@pytest.mark.it('The output should be the expected')
def test_output_print(capsys):
    from app import data_frame
    result = data_frame.empty == False and data.empty == False
    assert result == True
