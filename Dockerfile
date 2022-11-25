FROM python:3.10

ENV PYTHON_PIP_VERSION 10.0.1
ENV PIP_DEFAULT_TIMEOUT 120
ENV REQUESTS_CA_BUNDLE /etc/ssl/certs/pypl2.crt
ENV DEBIAN_FRONTEND noninteractive

COPY pypl2.crt /etc/ssl/certs/pypl2.crt

EXPOSE 5000
WORKDIR /app
RUN pip install flask
COPY . .
CMD [ "flask", "run", "--host", "0.0.0.0" ]