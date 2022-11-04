FROM python:3.9

WORKDIR /app/build

ENV PYTHONPATH /app/build/app

#RUN apt-get update -y && apt-get install -y --no-install-recommends \
#    default-libmysqlclient-dev && \
#    rm -rf /var/lib/apt/lists/*

RUN /usr/local/bin/python -m pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "settings.wsgi", "--threads", "2", \
     "--workers", "4", "--log-level", "debug", "--max-requests", \
     "1000", "--timeout", "10", "--bind=0.0.0.0:8000"]
#CMD ["python", "app/manage.py", "runserver", "0.0.0.0:8000"]
