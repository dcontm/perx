FROM python:3.6.9

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY needs.txt .
RUN pip install -r needs.txt

EXPOSE 8080

COPY . .

CMD python run.py
