FROM mcr.microsoft.com/mssql/server:2019-CU3-ubuntu-16.04
ENV ACCEPT_EULA Y
ENV SA_PASSWORD nzwnVWDDC0Oj
ENV MSSQL_PID Express
RUN mkdir /var/opt/mssql/backup
COPY ./SCHIPAnnualReports_2019-12-19.bak /var/opt/mssql/backup
COPY ./entrypoint.sh .
COPY ./setup.sql .

ENTRYPOINT [ "/bin/bash", "entrypoint.sh" ]
CMD [ "/opt/mssql/bin/sqlservr" ]