FROM python:3.7-alpine
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5001
CMD ["python", "flask_app.py"]
