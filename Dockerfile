FROM python:3.12 AS builder

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /task-app

RUN pip install poetry
RUN poetry config virtualenvs.in-project true
COPY pyproject.toml ./
RUN poetry install

FROM python:3.12-slim
RUN groupadd -r task_group && useradd -r -g task_group task_user

WORKDIR /task-app
COPY --from=builder /task-app/.venv .venv/
COPY . .

RUN chown -R task_user:task_group /task-app
USER task_user

CMD ["/task-app/.venv/bin/uwsgi", "--ini", "/task-app/uwsgi.ini"]
