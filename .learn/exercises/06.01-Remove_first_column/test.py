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
    assert captured.out == """      Id     Name  Year Gender State  Count
0  11350     Emma  2004      F    AK     62
1  11351  Madison  2004      F    AK     48
2  11352   Hannah  2004      F    AK     46
3  11353    Grace  2004      F    AK     44
4  11354    Emily  2004      F    AK     41
"""

