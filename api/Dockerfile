FROM python:3.9-slim

WORKDIR /api
COPY ./api/requirements.txt ./
RUN apt-get -y update && apt-get install -y default-libmysqlclient-dev build-essential gcc make libpq-dev pkg-config
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install --no-cache-dir configparser
RUN cp /usr/local/lib/python3.9/configparser.py /usr/local/lib/python3.9/ConfigParser.py
RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./api .
EXPOSE 8000
CMD ["uvicorn" , "main:app" , "--reload" , "--workers" , "1" , "--host" , "0.0.0.0" , "--port" , "8000"]
