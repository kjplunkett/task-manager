FROM python:3.12 AS python-builder

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /task-app

RUN pip install poetry
RUN poetry config virtualenvs.in-project true
COPY pyproject.toml ./
RUN poetry install

FROM node:20 AS node-builder

# Copy package.json
COPY package.json .

# Install Node dependencies
RUN npm install

# Copy the relevant frontend code
COPY ./public ./public
COPY ./src ./src

# Build the React app for production (output to /builds)
RUN npm run build

FROM python:3.12-slim

# Create non-root group and user to run uwsgi
RUN groupadd -r task_group && useradd -r -g task_group task_user

WORKDIR /task-app

# Copy the built backend
COPY --from=python-builder /task-app/.venv .venv/

# Copy the built frontend
COPY --from=node-builder /build /task-app/build

# Copy the app backend code
COPY ./app ./app

# Copy the uwsgi setup
COPY uwsgi.ini .
COPY wsgi.py .

# non root user owns everything under /task-app
RUN chown -R task_user:task_group /task-app

# Switch to non root user
USER task_user

# Start the uwsgi process
CMD ["/task-app/.venv/bin/uwsgi", "--ini", "/task-app/uwsgi.ini"]
