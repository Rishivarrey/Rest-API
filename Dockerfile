FROM nikolaik/python-nodejs:python3.8-nodej

WORKDIR /app

RUN apt-get update && apt-get install -y libpq-dev gcc
RUN  apt install libgirepository1.0-dev
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

RUN yarn --cwd staticsrc && yarn --cwd staticsrc build

RUN python3 manage.py collectstatic --no-input