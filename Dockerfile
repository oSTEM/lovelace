FROM python:3.9-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

COPY bot/ .

ENV token=$TOKEN

CMD ["python3", "./bot.py"]