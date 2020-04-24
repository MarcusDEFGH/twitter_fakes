FROM python:3.7.7
ENV PYTHONUNBUFFERED 1
LABEL maintainer="marcusvini211@gmail.com"

RUN apt-get update
RUN apt-get install -y locales
RUN echo "America/Recife" > /etc/timezone && \
    dpkg-reconfigure -f noninteractive tzdata && \
    sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    sed -i -e 's/# pt_BR.UTF-8 UTF-8/pt_BR.UTF-8 UTF-8/' /etc/locale.gen && \
    echo 'LANG="pt_BR.UTF-8"'>/etc/default/locale && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=pt_BR.UTF-8

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt


EXPOSE 8000