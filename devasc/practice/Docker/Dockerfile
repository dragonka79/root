FROM ubuntu:20.04

LABEL maintainer="dragonka79 dragonka79@gmail.com"

RUN apt-get update -y && apt-get install -y python3-pip python3-dev

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT ["python3"]

EXPOSE 5001
CMD [ "flask_to_container.py", "run","--host","0.0.0.0","--port","5000"]
