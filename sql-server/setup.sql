RESTORE DATABASE SCHIPAnnualReports
FROM DISK = '/var/opt/mssql/backup/SCHIPAnnualReports_2019-12-19.bak'
WITH MOVE 'SCHIPAnnualReports_dat' TO '/var/opt/mssql/data/SCHIPAnnualReports.mdf',
MOVE 'SCHIPAnnualReports_Index' TO '/var/opt/mssql/data/SCHIPAnnualReports_Index.ndf',
MOVE 'SCHIPAnnualReports_log' TO '/var/opt/mssql/data/SCHIPAnnualReports_Log.ldf'
GO