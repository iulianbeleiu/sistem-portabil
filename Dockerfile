FROM python:3.8-buster
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD . /sistem_portabil
WORKDIR /sistem_portabil
RUN pip install -e .