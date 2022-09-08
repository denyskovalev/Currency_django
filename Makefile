SHELL := /bin/bash

manage_py := python app/manage.py

run:
	$(manage_py) runserver 0:8000

make_migrations:
	$(manage_py) makemigrations

migrate:
	$(manage_py) migrate

celery_worker:
	cd app && celery -A settings worker --loglevel=INFO

celery_beat:
	cd app && celery -A settings beat --loglevel=INFO

shell_plus:
	$(manage_py) shell_plus --print-sql

build_migrate: make_migrations \
	migrate \
	run
