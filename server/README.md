# Back-End 🌶️

## Table of Contents

- [About](#about)
- [Getting Started](#getting-started)
- [Author](#author)

## About

The `Flask` 🌶️ project follows a RESTful API architectural style, emphasizing the principles of statelessness, resource identification, and uniform interface. By adhering to RESTful principles, the project aims to provide a clear and consistent approach to designing web services, promoting scalability, flexibility, and ease of maintenance.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Create the environment (creates a folder in your current directory)

```bash
virtualenv .venv
```

In Linux or Mac, activate the new python environment

```bash
source .venv/bin/activate
```

Or in Windows

```bash
source .venv/Scripts/activate
```

### Installing

CLI Init database

```bash
flask --app manage.py db init
```

CLI Makemigrations

```bash
flask --app manage.py db migrate -m "Initial migration"
```

CLI Migrate

```bash
flask --app manage.py db upgrade
```

File `.env`

```bash
SECRET_KEY=<secret_key>
```

CLI Runserver

```bash
py manage.py run --debug
```

## Author

Copyright &copy; 2024 by [ZIN](http://www.github.com/ZinF10)