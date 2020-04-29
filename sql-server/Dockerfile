# FROM mcr.microsoft.com/mssql/server:2019-CU3-ubuntu-16.04
FROM mcr.microsoft.com/mssql/server
RUN mkdir /var/opt/mssql/backup
COPY ./SCHIPAnnualReports_2019-12-19.bak /var/opt/mssql/backup
COPY ./entrypoint.sh .
COPY ./setup.sql .
# ENV ACCEPT_EULA Y
# ENV sa_password nzwnVWDDC0Oj
# RUN sqlcmd -E -S localhost –Q "RESTORE DATABASE SCHIPAnnualReports FROM DISK='/var/opt/mssql/backup/SCHIPAnnualReports_2019-12-19.bak'"

ENTRYPOINT [ "/bin/bash", "entrypoint.sh" ]
CMD [ "/opt/mssql/bin/sqlservr" ]