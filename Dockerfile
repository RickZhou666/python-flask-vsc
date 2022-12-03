FROM python:3.10

EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# Default powerline10k theme, no plugins installed [not working]
# RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.1.3/zsh-in-docker.sh)"

# enable bash auto-complete [not working]
# RUN apt-get update
# RUN apt-get install bash-completion -y

COPY . .
CMD [ "flask", "run", "--host", "0.0.0.0" ]