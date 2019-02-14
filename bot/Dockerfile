FROM python:3.7

WORKDIR /bot

COPY requirements.txt /bot
RUN pip3 install -r requirements.txt

COPY ./src /bot
CMD python3 __init__.py