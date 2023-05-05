FROM python:latest 

WORKDIR /

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8080

CMD [ "python", "main.py" ]