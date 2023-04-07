FROM gitpod/workspace-full:latest

USER gitpod

RUN pip3 install pytest==4.4.2 pytest-testdox mock numpy==1.17.4 pandas==0.25.3
RUN npm i @learnpack/learnpack -g && learnpack plugins:install learnpack-python@0.0.35

