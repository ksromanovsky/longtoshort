FROM python:latest
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT ['uwsgi']
CMD ['./uwsgi/app.ini']