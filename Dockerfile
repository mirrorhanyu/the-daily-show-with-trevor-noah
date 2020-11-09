FROM callmehan/python-ffmpeg

MAINTAINER Han Yu mirrorhanyu@gmail.com

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y imagemagick

RUN ["chmod", "+x", "./docker-entrypoint.sh"]

ENTRYPOINT ["./docker-entrypoint.sh"]
