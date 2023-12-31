FROM  python:3.11-slim-buster
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8080
ENV NAME World
CMD ["python", "app.py"]