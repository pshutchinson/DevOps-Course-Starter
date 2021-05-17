FROM python:3.9-slim-buster as base

# Install prerequisites
RUN apt-get update && apt-get install -y curl

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock* /

RUN poetry install

EXPOSE 5000

COPY ./ /

FROM base as production

ENTRYPOINT ["gunicorn"]
CMD ["--bind", "0.0.0.0:5000", "todo_app.app:create_app()"]

FROM base as development

ENV FLASK_APP=todo_app/app.py
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1 

ENTRYPOINT ["poetry"]
CMD ["run", "flask", "run", "--host=0.0.0.0"]