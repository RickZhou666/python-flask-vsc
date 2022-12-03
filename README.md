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

# sh -c "flask run" 
# above cmd line will tell server not using CMD line from Dockerfile but use flask run to start the server
$ docker run -dp 5000:5000 -w /app -v "$(pwd):/app" --name flask-smorest-api-rick rest-apis-flask-python sh -c "flask run"
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

<br><br><br>

##########################<br>
#### SETUP virtualenv<br>
##########################
1. create virtualenv
```bash
$ pyenv virtualenv 3.10.8 flask-vsc-3.10.8
```

2. list existing virtualenvs
$ pyenv virtualenvs
➜  python-flask-vsc git:(develop) ✗ pyenv virtualenvs
  3.10.8/envs/flask-vsc-3.10.8 (created from /Users/runzhou/.pyenv/versions/3.10.8)
  flask-vsc-3.10.8 (created from /Users/runzhou/.pyenv/versions/3.10.8)
>There are two entries for each virtualenv, and the shorter one is just a symlink.

3. activate your virtualenv
```bash
$ pyenv activate flask-vsc-3.10.8
$ pyenv deactivate
```

4. update pip
```bash
$ python3.10 -m pip install --upgrade pip
```

5. delete virtualenv
```bash
$ pyenv uninstall my-virtual-env
```

https://github.com/pyenv/pyenv-virtualenv

<br><br><br>

##########################<br>
SETUP local venv<br>
##########################
1. create local virtual env
$ python3.10 -m venv .venv

2. select interpreter
cmd + shift + P 

3. activate your virutal env
$ source .venv/bin/activate

<br><br><br>

##########################<br>
check flask<br>
##########################
$ which flask
(.venv) ➜  python-flask-vsc git:(develop) ✗ which flask
/Users/runzhou/git/python-flask-vsc/.venv/bin/flask


# 2. Deploy on gcp

1. ssh to your gcp machine
```bash
$ ssh 10.176.22.192
```

2. go to your home folder and create github pub key
```bash
$ cd /x/home/runzhou

$  ssh-keygen -t rsa -b 4096 -C "runzhou666@gmail.com"
```

3. clone repo to local
```bash
git clone git@github.com:RickZhou666/python-flask-vsc.git
```

4. check port avaialble to avoid conflict
```bash
sudo lsof -i -P -n | grep LISTEN
```

5. build docker image local
```bash
sudo docker build -t python-flask-vsc .
```

6. run in container
```bash
sudo docker run -dp 5000:5000 -w /app -v "$(pwd):/app" --restart=always --name python-flask-vsc_container python-flask-vsc
```
