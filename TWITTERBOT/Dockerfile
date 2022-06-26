FROM python:3.10.5

COPY config.ini /TWITTERBOT/
COPY tweebot.py /TWITTERBOT/
COPY TwitterAPI.py /TWITTERBOT/
COPY requirements.txt /tmp
COPY Dockerfile /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /TWITTERBOT
CMD ["python3", "tweebot.py"]