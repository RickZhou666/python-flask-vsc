# python-flask-vsc

## 1. Docker Command
### install dependencies
```bash
$ pip install -r requirements.txt
```
### build image
```bash
$ docker build -t rest-apis-flask-python .
```

### run image in a container
<!-- docker run --rm -d -p 127.0.0.1:5005:5000 --name flask-apis rest-apis-flask-python -->
1. use -v "$(pwd):/app" otherwise code changes is not reflected in docker container
```bash
$ docker run -dp 5000:5000 -w /app -v "$(pwd):/app" --name flask-smorest-api-rick rest-apis-flask-python
```

### display all images
```bash
$ docker images -a
```

### remove multiple images
```bash
$ docker image rm 8ae668a96ce6 aa4ecf532269 72d52a866646 2fa08ed06206 6840131c5619 7fb60d0ea30e 157095baba98
```

### display all container
```bash
$ docker ps -a 
```

### not able to use autocomplete with terminal inside docker container
[Ref](https://stackoverflow.com/questions/73013781/how-to-enable-autocomplete-when-connect-to-docker-container-through-cli)
try to login from terminal
```bash
$ docker exec -it <container-id> bash
$ docker exec -it f36a9e11f47e bash
```


##########################<br>
SETUP virtualenv<br>
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

##########################<br>
SETUP local venv<br>
##########################
# 1. create local virtual env
$ python3.10 -m venv .venv

# 2. select interpreter
cmd + shift + P 

# 5. activate your virutal env
$ source .venv/bin/activate


##########################<br>
check flask<br>
##########################
$ which flask
(.venv) ➜  python-flask-vsc git:(develop) ✗ which flask
/Users/runzhou/git/python-flask-vsc/.venv/bin/flask