FROM python:3.10.2-slim-bullseye

WORKDIR '/api'
COPY requirements.txt .
RUN apt-get -y update
RUN apt install -y build-essential
RUN apt-get -y install manpages-dev
RUN pip3 install --upgrade pip
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt
COPY . .



EXPOSE 7071

CMD ["python3", "app.py"]