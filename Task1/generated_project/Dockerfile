FROM python:3.11-slim
WORKDIR /app
RUN pip install --no-cache-dir Flask flask-cors gunicorn pytest==8.4.2 Pillow
COPY . .
EXPOSE 5000
CMD ["gunicorn", "app.main:app", "--bind", "0.0.0.0:5000"]
