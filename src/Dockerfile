FROM python:3.10.6
MAINTAINER byro team

EXPOSE 8020

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
    apt-get install -y zsh gettext libjpeg-dev libmagic-dev && \
    rm -rf /var/lib/apt/lists/*

RUN useradd uid1000 -d /home/uid1000
RUN mkdir -p /home/uid1000 && chown uid1000: /home/uid1000
RUN mkdir -p /byro && chown uid1000: /byro

ADD .. /byro/src
WORKDIR /byro/src
RUN cd /byro/src && pip3 install -e . && pip3 install gunicorn
RUN cd /byro/src && /bin/zsh install_local_plugins.sh

WORKDIR /byro/src

COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]