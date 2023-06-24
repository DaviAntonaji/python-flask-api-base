FROM python:3.10.2-alpine

ARG PORT

WORKDIR '/api'
COPY requirements.txt .

RUN apk update && \
    apk add --no-cache build-base && \
    apk add --no-cache man-pages

RUN pip install --upgrade pip && \
    pip install --trusted-host pypi.python.org -r requirements.txt

COPY . .

EXPOSE ${PORT}

CMD ["python3", "app.py"]
