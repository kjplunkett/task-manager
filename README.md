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

- [ ] Flask API - CRUDL operations (in memory with a dictionary for state)
- [ ] Add persistence with SQLite
- [ ] Add React frontend with Bootstrap styles
- [ ] Add Tests
- [ ] Deploy
