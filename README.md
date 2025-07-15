### Hexlet tests and linter status:
[![Actions Status](https://github.com/MrMAx-26/python-project-83/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/MrMAx-26/python-project-83/actions)
[![Python CI](https://github.com/MrMAx-26/python-project-83/actions/workflows/pyci.yml/badge.svg)](https://github.com/MrMAx-26/python-project-83/actions/workflows/pyci.yml)
[![Maintainability](https://qlty.sh/gh/MrMAx-26/projects/python-project-83/maintainability.svg)](https://qlty.sh/gh/MrMAx-26/projects/python-project-83)

[Please visit my Page analyzer on render.com](https://python-project-83-jh1a.onrender.com)

### Description
Webpage Analyzer is an online tool that assesses the compatibility of web pages with SEO practices, much like the functionality offered by PageSpeed Insights.

This is project ["Page analyzer"](https://ru.hexlet.io/programs/python/projects/83) on the Python Development course on [Hexlet.io](https://ru.hexlet.io/programs/python)

### Used technologies:
This project was built using these tools:

| Tool                                                                        | Description                                             |
|-----------------------------------------------------------------------------|---------------------------------------------------------|
| [uv](https://docs.astral.sh/uv/)                                        | "is an extremely fast Python package manager written in Rust. It is designed as a replacement for pip and pip-tools. It can also replace venv and pyenv."  |            |
| [ruff](https://docs.astral.sh/ruff/)               | "Your Tool For Linter and Style Guide Enforcement"|
| [Flask](https://flask.palletsprojects.com/en/stable/)               | "Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications" |
| [Gunicorn](https://docs.gunicorn.org/en/latest/index.html)                                        | "Gunicorn ‘Green Unicorn’ is a Python WSGI HTTP Server for UNIX. It’s a pre-fork worker model ported from Ruby’s Unicorn project. The Gunicorn server is broadly compatible with various web frameworks, simply implemented, light on server resources, and fairly speedy."  |
| [python-dotenv](https://pypi.org/project/python-dotenv/)                                        | "Python-dotenv reads key-value pairs from a .env file and can set them as environment variables. It helps in the development of applications following the 12-factor principles."  |
| [Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/)                                        | "Bootstrap is a powerful, feature-packed frontend toolkit. Build anything—from prototype to production—in minutes."  |
| [Psycopg](https://getbootstrap.com/docs/5.3/getting-started/introduction/)                                        | "Psycopg – PostgreSQL database adapter for Python"  |
| [validators](https://validators.readthedocs.io/en/latest/#module-validators.url)                                        | "Python Data Validation for Humans™."  |
| [Requests](https://requests.readthedocs.io/en/latest/)                                        | "Requests is an elegant and simple HTTP library for Python, built for human beings."  |
| [Beautifulsoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)                                        | "Beautiful Soup is a Python library for pulling data out of HTML and XML files."  |

## Installation
### Clone the repo:
```
git clone git@github.com:MrMAx-26/python-project-83
cd python-project-83
```
### To use the app properly you'll need to provide it with $DATABASE_URL and $SECRET_KEY vars.
To deploy the application, you need to rename the .env-sample file to .env in the root directory. After that, modify the values for SECRET_KEY and DATABASE_URL. It is important to insert your own values.

### After that run: make build to install all required packages and create necessary tables in the database.
```
make build
```
### Run make start to start.

```
make start
```