FROM python

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/src/Online_Store

WORKDIR /usr/src/Online_Store

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000