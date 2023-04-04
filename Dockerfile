FROM python:3.9.16

RUN pip install flask 
WORKDIR /app
COPY ./app/ .

ENTRYPOINT ["python3" ,"app.py"]

