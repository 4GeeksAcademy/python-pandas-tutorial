import sys, os, json
if os.path.isdir("./.venv/lib/"):
    sys.path.append('./.venv/lib/python3.8/site-packages')
def pytest_addoption(parser):
    parser.addoption("--stdin", action="append", default=[],
        help="json with the stdin to pass to test functions")
def pytest_generate_tests(metafunc):
    if 'stdin' in metafunc.fixturenames:
      if hasattr(metafunc,"config"):
          metafunc.parametrize("stdin",metafunc.config.getoption('stdin'))
      elif hasattr(metafunc,"configuration"):
          metafunc.parametrize("stdin",metafunc.configuration.getoption('stdin'))
      else:
          raise Exception("Imposible to retrieve text configuration object")
    if 'app' in metafunc.fixturenames:
        try:
          sys.path.append('.learn/dist')
          import cached_app
          metafunc.parametrize("app",[cached_app.execute_app])
        except SyntaxError:
          metafunc.parametrize("app",[lambda : None])
        except ImportError:
          metafunc.parametrize("app",[cached_app])
        except AttributeError:
          metafunc.parametrize("app",[cached_app])
    if 'configuration' in metafunc.fixturenames:
        metafunc.parametrize("configuration", [json.loads('{"port":3000,"address":"https://kiddopro-pythonpandastu-mcial2n3lf7.ws-us41.gitpod.io","editor":{"mode":"preview","agent":"gitpod","version":"1.0.72"},"dirPath":"./.learn","configPath":"learn.json","outputPath":".learn/dist","publicPath":"/preview","publicUrl":"https://3000-kiddopro-pythonpandastu-mcial2n3lf7.ws-us41.gitpod.io","language":"auto","grading":"incremental","exercisesPath":".learn/exercises","webpackTemplate":null,"disableGrading":false,"disabledActions":["build"],"actions":[],"entries":{"html":"index.html","vanillajs":"index.js","react":"app.jsx","node":"app.js","python3":"app.py","java":"app.java"},"preview":"https://github.com/4GeeksAcademy/python-pandas-tutorial/blob/main/.learn/assets/pandas-preview.jpeg?raw=true","difficulty":"beginner","duration":3,"description":"Learn the basics and become comfortable using pandas for manipulating machine learning datasets .","title":"Pandas for Machine Learning","slug":"pandas-for-machine-learning","session":6793656476394450000,"translations":[]}')])
