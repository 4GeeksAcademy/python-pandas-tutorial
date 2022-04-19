import pytest, os, re, io, sys

@pytest.mark.it('Create a file named app.py')
def test_file_existence():
    file = os.path.abspath(__file__)+'/app.py'
    assert file != None

@pytest.mark.it("Use the print function")
def test_output():
    f = open(os.path.dirname(os.path.abspath('app.py'))+'/app.py')
    content = f.read()
    assert content.find("print(") > 0

@pytest.mark.it('The output should be the expected: Hello World')
def test_print(capsys):
    import app
    captured = capsys.readouterr()
    assert captured.out == 'Hello World\n' 