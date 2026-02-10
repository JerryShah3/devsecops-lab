FROM python:3.9-slim

WORKDIR /app
COPY . .
RUN pip install flask==1.0
CMD ["python", "app.py"]

