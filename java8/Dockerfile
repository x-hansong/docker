FROM debian:jessie
MAINTAINER Hansong Xiao <x.hansong.scut@gmail.com>

RUN echo "deb http://mirrors.163.com/debian/ jessie main non-free contrib" > /etc/apt/sources.list

RUN \
    export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get upgrade -y && \
    echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee /etc/apt/sources.list.d/webupd8team-java.list && \
    echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu precise main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 && \
    apt-get update && \
    apt-get -y install locales && \
    sed -i.bak -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen && \
    update-locale LC_ALL= "en_US.UTF-8" && \
    export LANGUAGE=en_US:en && \
    export LANG=en_US.UTF-8 && \
    export LC_ALL=en_US.UTF-8 && \
    dpkg-reconfigure locales && \
    echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections && \
    apt-get -y install oracle-java8-installer && \
    update-alternatives --display java && \
    apt-get -y install oracle-java8-set-default && \
    rm -fr /var/cache/oracle-jdk8-installer && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV LANG       en_US.UTF-8
ENV LC_ALL     en_US.UTF-8
ENV LANGUAGE   en_US:en

ENV JAVA_HOME /usr/lib/jvm/java-8-oracle
