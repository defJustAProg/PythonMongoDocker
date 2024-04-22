FROM mongo:latest
ADD . /dbdir
WORKDIR /dbdir
RUN apt-get update && \
    apt-get install -y python3-pip
COPY . .