FROM callmehan/python-ffmpeg

MAINTAINER Han Yu mirrorhanyu@gmail.com

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y imagemagick

RUN sed -i "/@*/d" /etc/ImageMagick-6/policy.xml

RUN ["chmod", "+x", "./docker-entrypoint.sh"]

ENTRYPOINT ["./docker-entrypoint.sh"]
