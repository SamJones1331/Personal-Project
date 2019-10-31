FROM ubuntu:16.04

RUN apt-get update -y
RUN apt-get install python3-pip -y

COPY . .

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "run.py"]
