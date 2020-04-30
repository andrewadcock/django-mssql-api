# CARTS / SEDS Dockerized POC

## Required Setup

- SCHIPAnnualReports_2019-12-19.bak placed in sql-server directory

## Usage

- Default user is "admin:password123"
- Navigate to localhost:8000

## API Notes

- Users and Groups endpoints are from Postgres for user management
- Questions, Sections, Answers, States, StatePrograms, and QuestionsAnswers are from SQL Server CARTS/SEDS backup
- Questions, Answers, StatePrograms, and QuestionsAnswers are not working right now

## Other Notes

Basic Django + Postgres Framework

- https://docs.docker.com/compose/django/
- https://www.django-rest-framework.org/

SQL Server

- Connect to Microsoft SQL Server You can connect to the SQL Server using the sqlcmd tool inside of the container by using the following command on the host:
  - docker exec -it <container_id|container_name> /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P <your_password>
  - https://docs.microsoft.com/en-us/sql/ssms/scripting/sqlcmd-use-the-utility?view=sql-server-ver15
