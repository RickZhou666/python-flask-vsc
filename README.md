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