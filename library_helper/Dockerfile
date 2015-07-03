FROM ubuntu:14.04
MAINTAINER xiaohansong

#RUN echo "deb http://mirrors.163.com/ubuntu/ precise main restricted universe multiverse" > /etc/apt/sources.list
#RUN apt-get update
RUN apt-get install -y python
EXPOSE 1234
ADD ./library.py /root/
WORKDIR /root
ENTRYPOINT ["python"]
CMD ["library.py"]
