import pytest, os, re, io, sys

@pytest.mark.it('Create a file named app.py')
def test_file_existence():
    file = os.path.exists('app.py')
    assert file == True

@pytest.mark.it("Use the print function")
def test_output():
    f = open('app.py')
    content = f.read()
    assert "print" in content

@pytest.mark.it('The output should be the expected: Hello World')
def test_print(capsys):
    import app
    captured = capsys.readouterr()
    assert  'Hello World\n' in captured.out