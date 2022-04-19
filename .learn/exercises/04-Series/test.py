import pytest, re, os, io, sys

@pytest.mark.it('You must import pandas')
def test_import_pandas():
    path = os.path.dirname(os.path.abspath('app.py'))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"import\s*pandas")
        assert bool(regex.search(content)) == True

@pytest.mark.it('The variable ages must exist')
def test_vatiable_existence():
    from app import ages

@pytest.mark.it('The output should be the expected')
def test_expected_output(capsys):
    import app
    captured = capsys.readouterr()
    assert captured.out == """0    23
1    45
2     7
3    34
4     6
5    63
6    36
7    78
8    54
9    34
dtype: int64

"""