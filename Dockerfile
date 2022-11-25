FROM python:3.10

ENV PYTHON_PIP_VERSION 10.0.1
ENV PIP_DEFAULT_TIMEOUT 120
ENV REQUESTS_CA_BUNDLE /etc/ssl/certs/pypl2.crt
ENV DEBIAN_FRONTEND noninteractive

COPY pypl2.crt /etc/ssl/certs/pypl2.crt
# COPY pypl2.crt /etc/ssl/certs/pypl2.crt

EXPOSE 5000
WORKDIR /app
# COPY ./etc . 
RUN pip install flask
# RUN pip install flask -i https://pypi.tuna.tsinghua.edu.cn/simple --default-timeout=1000 flask
COPY . .
CMD [ "flask", "run", "--host", "0.0.0.0" ]