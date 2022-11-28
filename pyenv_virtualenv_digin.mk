##########################
#### SETUP virtualenv ####
##########################
# 1. create virtualenv
$ pyenv virtualenv 3.10.8 flask-vsc-3.10.8

# 2. list existing virtualenvs
$ pyenv virtualenvs
➜  python-flask-vsc git:(develop) ✗ pyenv virtualenvs
  3.10.8/envs/flask-vsc-3.10.8 (created from /Users/runzhou/.pyenv/versions/3.10.8)
  flask-vsc-3.10.8 (created from /Users/runzhou/.pyenv/versions/3.10.8)
#   There are two entries for each virtualenv, and the shorter one is just a symlink.


# 3. activate your virtualenv
$ pyenv activate flask-vsc-3.10.8
$ pyenv deactivate

# update pip
$ python3.10 -m pip install --upgrade pip


# 4. delete virtualenv
$ pyenv uninstall my-virtual-env


https://github.com/pyenv/pyenv-virtualenv

##########################
#### SETUP local venv ####
##########################
# 1. create local virtual env
$ python3.10 -m venv .venv

# 2. select interpreter
cmd + shift + P 

# 5. activate your virutal env
$ source .venv/bin/activate


##########################
###### check flask #######
##########################
$ which flask
(.venv) ➜  python-flask-vsc git:(develop) ✗ which flask
/Users/runzhou/git/python-flask-vsc/.venv/bin/flask