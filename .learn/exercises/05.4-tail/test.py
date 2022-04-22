import io, os, re, sys, pytest, pandas
data_frame = pandas.read_csv('.learn/assets/pokemon_data.csv').tail(3)

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
    assert content.find("print") > 0


@pytest.mark.it('The output should be the expected')
def test_expected_output(capsys):
    import app
    captured = capsys.readouterr()
    assert captured.out == str(data_frame)+'\n'

# @pytest.mark.it('The variable data_frame should exist')
# def test_variable_existence():
#     from app import data_frame

"""       #                 Name   Type 1 Type 2  HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary
797  720  HoopaHoopa Confined  Psychic  Ghost  80     110       60      150      130     70           6       True
798  720   HoopaHoopa Unbound  Psychic   Dark  80     160       60      170      130     80           6       True
799  721            Volcanion     Fire  Water  80     110      120      130       90     70           6       True
"""