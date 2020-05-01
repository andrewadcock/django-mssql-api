FROM ubuntu:16.04
RUN apt-get update
RUN apt-get install python3 python3-pip -y
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
USER root

RUN apt-get install -y unixodbc-dev dos2unix

RUN apt-get install libpq-dev -y
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt

RUN apt-get install curl -y
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN echo "deb [arch=amd64] https://packages.microsoft.com/ubuntu/16.04/prod bionic main" | tee /etc/apt/sources.list.d/mssql-release.list

RUN apt-get install wget libcurl3 libc6 libstdc++6 libkrb5-3 openssl debconf unixodbc unixodbc-dev -y
RUN wget https://packages.microsoft.com/ubuntu/16.04/prod/pool/main/m/msodbcsql/msodbcsql_13.1.9.2-1_amd64.deb
RUN yes | ACCEPT_EULA=Y dpkg -i msodbcsql_13.1.9.2-1_amd64.deb

COPY . /code/
RUN dos2unix ./start.sh && apt-get --purge remove -y dos2unix && rm -rf /var/lib/apt/lists/