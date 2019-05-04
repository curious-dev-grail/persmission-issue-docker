FROM python:3.6
ADD src/requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt
ADD . /usr/app
WORKDIR /usr/app/src/
ENTRYPOINT ["python3"]
CMD ["app.py"]
