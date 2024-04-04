## Django + MSSQL Server + Docker
From django access to Microsoft SQL server in docker.

## Init.
Create a new .env file as in the .env.example example and fill it with the connection parameters to the MSSQL server. Select the desired MSSQL Server connection driver, version 17 or 18 by editing the settings:

for 17 version driver
```
"OPTIONS": {"driver": "ODBC Driver 17 for SQL Server", },

```

for 18 version driver
```
'OPTIONS': {
            'driver': "ODBC Driver 18 for SQL Server",
            'extra_params': "Encrypt=no;TrustServerCertificate=yes",
        },
```

and Dockerfile:

for 17 version driver
```
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -  && \
     curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update && \
     ACCEPT_EULA=Y apt-get install -y msodbcsql17 unixodbc-dev libgssapi-krb5-2

```

for 18 version driver
```
RUN curl https://packages.microsoft.com/keys/microsoft.asc | tee /etc/apt/trusted.gpg.d/microsoft.asc  && \
    curl https://packages.microsoft.com/config/debian/11/prod.list | tee /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql18 unixodbc-dev libgssapi-krb5-2
```

## How to run.
```
$ docker-compose build
$ docker-compose up -d
```



