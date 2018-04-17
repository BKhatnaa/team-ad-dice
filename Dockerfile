FROM ubuntu:latest
MAINTAINER Rajdeep Dua "dua_rajdeep@yahoo.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
WORKDIR /app
ADD requirements.txt /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
