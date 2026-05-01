FROM python:3.7-alpine

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install flask pytz

EXPOSE 5000

CMD ["python", "index.py"]