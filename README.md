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

## TODO

- [x] Flask API w/ CRUDL operations (in memory)
- [x] Add API tests
- [ ] Add SQLAlchemy models, connection, and queries w/ SQLite db
- [ ] Add React frontend w/ Bootstrap styles
- [ ] Add Frontend tests
- [ ] Deploy
