# Task Manager

## Development

Prerequisites:
- [Poetry](https://python-poetry.org/) installed
- [Poe The Poet](https://poethepoet.natn.io/) installed

Install Python dependencies:
```shell
poetry install
```

Lint:
```shell
poe lint
```

Format:
```shell
poe format
```

Test:
```shell
poe test
```

Start the API server:
```shell
poe start
```

Vist the URL in your browser to get a 200 response with an empty JSON array (no tasks yet)
```shell
http://127.0.0.1:5000/tasks
```

## TODO

- [x] Flask API w/ CRUDL operations (in memory)
- [x] Add API tests
- [x] Add SQLAlchemy connection for SQLite DB 
- [x] Add SQLAlchemy models and queries, connection, and queries w/ SQLite db
- [ ] Add React frontend w/ Bootstrap styles
- [ ] Add Frontend tests
- [ ] Deploy
