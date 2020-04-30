FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN apt-get update
RUN apt-get install -y unixodbc-dev
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY install-driver.sh /code/
RUN bash install-driver.sh
COPY . /code/