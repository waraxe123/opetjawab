FROM python:3.9.5-buster

RUN apt-get update && apt-get upgrade -y

#Installing Requirements
RUN apt-get install -y python3-pip

#Updating pip
RUN python3.9 -m pip install -U pip


RUN python3.9 -m pip install -U -r requirements.txt

CMD python3 main.py
