FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /var/www/html/
ADD django_pro /var/www/html/
RUN python3 -m venv myvenv
RUN . myvenv/bin/activate
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pwd
RUN ls -lrth
CMD python manage.py runserver 0.0.0.0:8000
