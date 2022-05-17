import os, io, json, pytest, sys, json

@pytest.mark.it("Install pandas package: pipenv install pandas")
def test_output():
    f = open(os.path.dirname(os.path.abspath('Pipfile.lock')+'/Pipfile.lock'))
    content = f.read()
    assert content.find("pandas") > 0