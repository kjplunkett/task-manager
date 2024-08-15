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

Run the API server on port 8000:
```shell
poe start
```

Visit the URL in your browser and you should get a 200 response with an empty JSON array (no tasks yet)
```shell
http://localhost:8000/tasks
```

## TODO

- [x] Flask API w/ CRUDL operations (in memory)
- [x] Add API tests
- [x] Add SQLAlchemy connection for SQLite DB 
- [ ] Add SQLAlchemy models and queries, connection, and queries w/ SQLite db
- [ ] Add React frontend w/ Bootstrap styles
- [ ] Add Frontend tests
- [ ] Deploy
