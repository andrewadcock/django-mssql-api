FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
USER root
RUN apt-get update
RUN apt-get install -y unixodbc-dev dos2unix
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN echo "deb [arch=amd64] https://packages.microsoft.com/ubuntu/18.04/prod bionic main" | tee /etc/apt/sources.list.d/mssql-release.list
RUN apt update
RUN yes | ACCEPT_EULA=Y apt install msodbcsql17
COPY . /code/
RUN dos2unix ./start.sh && apt-get --purge remove -y dos2unix && rm -rf /var/lib/apt/lists/