FROM ubuntu:16.04

RUN apt-get update -y
RUN apt-get install python3-pip -y
RUN apt install -y netcat

COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .

ENTRYPOINT ["./init.sh"]
