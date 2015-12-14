FROM java:8
MAINTAINER Hansong Xiao <x.hansong.scut@gmail.com>

ENV GRADLE_VERSION 2.6

RUN apt-get update && apt-get -y install wget unzip

WORKDIR /usr/bin
RUN wget  https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-all.zip && \
  unzip gradle-${GRADLE_VERSION}-all.zip && \
  ln -s gradle-${GRADLE_VERSION} gradle && \
  rm gradle-${GRADLE_VERSION}-all.zip

ENV GRADLE_HOME /usr/bin/gradle
ENV PATH $PATH:$GRADLE_HOME/bin

RUN mkdir /app
WORKDIR /app

ENTRYPOINT ["gradle"]
CMD ["-version"]
