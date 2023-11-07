FROM python:3.11-slim
 
RUN apt update

WORKDIR /bahis/oidc/

RUN pip install pipenv==2023.9.8
COPY Pipfile Pipfile.lock ./
RUN pipenv sync --system -v

CMD python manage.py collectstatic --noinput && gunicorn --workers=4 --threads=1 -b 0.0.0.0:80 oidc.wsgi
