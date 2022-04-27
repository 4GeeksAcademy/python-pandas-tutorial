import io, os, re, sys, pytest

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
    assert "print(" in content


@pytest.mark.it('The output should be the expected.')
def test_expected_output(capsys):
    import app
    captured = capsys.readouterr()
    assert captured.out == """    Brand    Model   Color
0  Toyota  Corolla    Blue
1    Ford        K  Yellow
2  Porche  Cayenne   White
"""

@pytest.mark.it('The variable data should exist')
def test_variable_existence():
    from app import data