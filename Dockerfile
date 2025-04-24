FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Zorg dat het script uitvoerbaar is
RUN chmod +x entrypoint.sh

EXPOSE 8000

# Gebruik het script als startpunt
CMD ["./entrypoint.sh"]
