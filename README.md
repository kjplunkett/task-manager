# Task Manager

Demo: https://northspyre-take-home.fly.dev/

<img alt="image" src="https://github.com/user-attachments/assets/7fa70582-b28e-43b0-9bdf-368577b2a935">

## Development

### Backend
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
http://127.0.0.1:8080/tasks
```

### Frontend

Prerequisites:
- [Node 20](https://nodejs.org/en/download/package-manager) installed

Install Node dependencies:
```shell
npm i
```

Start the webpack dev server:
```shell
npm start
```

## TODO

- [x] Flask API w/ CRUDL operations (in memory)
- [x] Add API tests
- [x] Add SQLAlchemy + SQLite DB 
- [x] Add models + validation & serialization
- [x] Add React frontend w/ Bootstrap styles
- [x] Deploy (Github Actions to Fly.io)
