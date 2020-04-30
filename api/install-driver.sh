# https://askubuntu.com/questions/1129309/unable-to-install-msodbcsql17-on-ubuntu-18-04
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
echo "deb [arch=amd64] https://packages.microsoft.com/ubuntu/18.04/prod bionic main" | tee /etc/apt/sources.list.d/mssql-release.list
apt update
yes | ACCEPT_EULA=Y apt install msodbcsql17