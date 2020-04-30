# CARTS / SEDS Dockerized POC

## Required Setup

SCHIPAnnualReports_2019-12-19.bak placed in sql-server directory
Default user is "admin:password123"

## Notes

Basic Django + Postgres Framework

- https://docs.docker.com/compose/django/

SQL Server

- Connect to Microsoft SQL Server You can connect to the SQL Server using the sqlcmd tool inside of the container by using the following command on the host:
  - docker exec -it <container_id|container_name> /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P <your_password>
  - https://docs.microsoft.com/en-us/sql/ssms/scripting/sqlcmd-use-the-utility?view=sql-server-ver15
