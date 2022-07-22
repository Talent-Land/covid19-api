FROM ubuntu:18.04

RUN apt update -y  &&  apt upgrade -y && apt-get update 

RUN apt-get -y install python3
RUN apt-get -y install python3-pip
RUN apt install -y curl git openjdk-8-jdk unixodbc-dev

# Add SQL Server ODBC Driver 17 for Ubuntu 18.04
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y --allow-unauthenticated msodbcsql17
RUN ACCEPT_EULA=Y apt-get install -y --allow-unauthenticated mssql-tools
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc

COPY startup.sh /
RUN chmod +x /startup.sh
ENTRYPOINT ["sh","/startup.sh"]

RUN ["pip3", "install", "numpy"]
RUN ["pip3", "install", "pandas"]
RUN ["pip3", "install", "python-dateutil"]
RUN ["pip3", "install", "pickleshare"]
RUN ["pip3", "install", "sentence-transformers"]
RUN ["pip3", "install", "pickleshare"]
RUN ["pip3", "install", "torch"]
RUN ["pip3", "install", "Flask"]
RUN ["pip3", "install", "Flask-Compress"]
RUN ["pip3", "install", "pyodbc"]


RUN mkdir /home/prj