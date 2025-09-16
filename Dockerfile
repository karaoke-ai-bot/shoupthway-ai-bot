
# shoupthway-ai-bot

Complex AI Bot Prototype
# Python base image
FROM python:3.10-slim

# working directory
WORKDIR /app

# copy requirements (later we can add requirements.txt)
COPY requirements.txt requirements.txt

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy app
COPY . .

# run the app
CMD ["python", "app/main.py"]
