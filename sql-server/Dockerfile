FROM mcr.microsoft.com/mssql/server:2019-CU3-ubuntu-16.04
ENV ACCEPT_EULA Y
ENV SA_PASSWORD nzwnVWDDC0Oj
ENV MSSQL_PID Express
USER root
RUN apt update && apt install -y dos2unix
RUN mkdir /var/opt/mssql/backup
COPY ./SCHIPAnnualReports.bak /var/opt/mssql/backup
COPY ./entrypoint.sh .
COPY ./setup.sql .
RUN dos2unix ./entrypoint.sh && apt-get --purge remove -y dos2unix && rm -rf /var/lib/apt/lists/

ENTRYPOINT [ "/bin/bash", "entrypoint.sh" ]
CMD [ "/opt/mssql/bin/sqlservr" ]