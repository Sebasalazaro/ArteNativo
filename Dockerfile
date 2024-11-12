FROM python:3.12-alpine3.17

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=ArteNativo.settings

WORKDIR /usr/app/arte-nativo

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 80

RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]

CMD [ "python", "manage.py", "runserver", "0.0.0.0:80"]
