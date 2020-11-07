FROM callmehan/python-ffmpeg

MAINTAINER Han Yu mirrorhanyu@gmail.com

WORKDIR /app

COPY . .

RUN ["chmod", "+x", "./docker-entrypoint.sh"]

ENTRYPOINT ["./docker-entrypoint.sh"]
