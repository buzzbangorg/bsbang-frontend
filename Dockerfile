FROM alpine:3.5
RUN apk add --update python3
RUN apk add --update py3-pip
COPY requirements.txt /usr/src/app/
RUN pip3 install --no-cache-dir -r /usr/src/app/requirements.txt
COPY app.py /usr/src/app/
COPY templates/index.html /usr/src/app/templates/
EXPOSE 5000
CMD ["python3", "/usr/src/app/app.py"]
