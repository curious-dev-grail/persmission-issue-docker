FROM python:3.6
ADD src/requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt
#added groupid argument with default value 9000 which can be manipulated while building image
ARG gid=9000
#added userid argument with default value 9000 which can be manipulated while building image 
ARG uid=9000
#added new user dockerize with user id uid and group id gid
RUN addgroup --gid $gid  dockerize && \
    adduser --uid $uid --ingroup dockerize --home /home/dockerize --shell /bin/sh --disabled-password --gecos "" dockerize 
ADD . /usr/app/
WORKDIR /usr/app/src/
#activate the user dockerize
USER dockerize
ENTRYPOINT ["python3"]
CMD ["app.py"]
