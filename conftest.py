import sys, os, json
if os.path.isdir("./.venv/lib/"):
    sys.path.append('null/site-packages')
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
        metafunc.parametrize("configuration", [json.loads('{"port":3000,"os":"linux","editor":{"mode":"extension","agent":"vscode","version":"3.1.36"},"dirPath":"./.learn","configPath":"learn.json","outputPath":".learn/dist","publicPath":"/preview","publicUrl":"https://orange-space-tribble-97q5q9j7467wfpp6v-3000.app.github.dev","contact":"https://github.com/learnpack/learnpack/issues/new","language":"auto","autoPlay":true,"projectType":"tutorial","grading":"incremental","exercisesPath":".learn/exercises","webpackTemplate":null,"disableGrading":false,"disabledActions":["build"],"actions":[],"entries":{"html":"index.html","vanillajs":"index.js","react":"app.jsx","node":"app.js","python3":"app.py","java":"app.java"},"preview":"https://github.com/4GeeksAcademy/python-pandas-tutorial/blob/main/.learn/assets/pandas-preview.jpeg?raw=true","difficulty":"beginner","duration":3,"description":{"us":"Learn the basics and become comfortable using pandas for manipulating machine learning datasets.","es":"Aprende lo básico y empieza a sentirte cómodo usando pandas y manipulando datasets de machine learning."},"title":{"us":"Pandas for Machine Learning","es":"Pandas para Machine Learning"},"slug":"pandas-for-machine-learning","telemetry":{"batch":"https://breathecode.herokuapp.com/v1/assignment/me/telemetry"},"translations":[]}')])
