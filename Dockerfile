#THIS WORKS

#FROM python:3.9-slim-buster

# Install prerequisites
#RUN apt-get update && apt-get install -y curl

# Install Poetry
#RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
#    cd /usr/local/bin && \
#    ln -s /opt/poetry/bin/poetry && \
#    poetry config virtualenvs.create false

#COPY pyproject.toml poetry.lock* /

#RUN poetry install

#ENV FLASK_APP=todo_app/app.py
#ENV FLASK_ENV=development
#COPY ./ /

#EXPOSE 5000

#ENTRYPOINT ["poetry"]
#CMD ["run", "flask", "run", "--host=0.0.0.0"]





FROM python:3.9-slim-buster

# Install prerequisites
RUN apt-get update && apt-get install -y curl gunicorn

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock* /

RUN poetry install

ENV FLASK_APP=todo_app/app.py
ENV FLASK_ENV=development

COPY ./ /

EXPOSE 5000

ENTRYPOINT ["gunicorn"]
CMD ["--bind", "0.0.0.0:5000", "todo_app.app:app"]