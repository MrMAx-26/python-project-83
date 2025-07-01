PORT ?= 5000
postgresql:
	sudo service postgresql start

install:
	uv sync
dev:
	uv run flask --debug --app page_analyzer:app run
check:
	uv run ruff check .
check-fix:
	uv run ruff check --fix .

start:
	uv run gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app
build:
	./build.sh
render-start:
	gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app
