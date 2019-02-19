FROM python:3.7

WORKDIR /app

COPY requirements.txt /app
RUN pip3 install -r requirements.txt

COPY ./src /app

CMD ["python3", "bot.py"]

