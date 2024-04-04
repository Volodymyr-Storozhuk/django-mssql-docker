# install basic image
FROM python:3.11-slim-buster

# about project
LABEL maintainer="Volodymyr Storozhuk volodymyr.storozhuk@hotmail.com"

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get install -y gnupg2 curl 

# Add Microsoft SQL Server ODBC Driver 17 driver
# RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -  && \
#     curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list
# RUN apt-get update && \
#     ACCEPT_EULA=Y apt-get install -y msodbcsql17 unixodbc-dev libgssapi-krb5-2

# Add Microsoft SQL Server ODBC Driver 18 driver
RUN curl https://packages.microsoft.com/keys/microsoft.asc | tee /etc/apt/trusted.gpg.d/microsoft.asc  && \
    curl https://packages.microsoft.com/config/debian/11/prod.list | tee /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql18 unixodbc-dev libgssapi-krb5-2

# users uid gid
ARG UID=1000
ARG GIT=1000
ENV UID=${UID}
ENV GID=${GID}

# add user
RUN useradd -m -u $UID www
USER www

# work dir
# WORKDIR /usr/src/app/
WORKDIR /home/www/web/

# cp project and copy requiremets
COPY requirements.txt .
RUN pip install --no-cache -r requirements.txt
#  cp project
COPY . .