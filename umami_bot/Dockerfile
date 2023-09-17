FROM python:3.11.5

WORKDIR /usr/umami_bot

ENV POETRY_VERSION=1.6.1

COPY pyproject.toml ./
COPY poetry.lock ./

# Installation of Poetry and application dependencies
RUN : \
    && pip install --ignore-installed "poetry==${POETRY_VERSION}" \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi \
    && :

COPY src .

COPY .env .
COPY logging_config.yaml .

COPY scripts .
COPY tests .

ENV PYTHONPATH="${PYTHONPATH}:/usr/umami_bot/src"

CMD ["bash", "./scripts/start_app.sh"]
