FROM python:3.8

WORKDIR /pythonProject

COPY . .

CMD ["python", "/pythonProject/hello.py"]