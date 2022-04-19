import pytest, os, re, io, sys

@pytest.mark.it('Create a file named app.py')
def test_file_existence():
    file = os.path.abspath(__file__)+'/app.py'
    assert file != None

@pytest.mark.it('Use print function')
def test_print(capsys):
    import app
    captured = capsys.readouterr()
    assert captured.out == 'Hello World\n' 