FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./
COPY .env ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5001

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5001"]