FROM python:3.9

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt --no-cache-dir

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "conf.wsgi:application", "--bind", "0:8000" ]
