SHELL := /bin/bash

manage_py := docker exec -it backend python app/manage.py

run:
	$(manage_py) runserver 0:8000

make_migrations:
	$(manage_py) makemigrations

migrate:
	$(manage_py) migrate

celery_worker:
	celery -A settings worker --loglevel=INFO

celery_beat:
	celery -A settings beat --loglevel=INFO

shell_plus:
	$(manage_py) shell_plus --print-sql

build_migrate: make_migrations \
	migrate \
	run

flake8:
	flake8 app/

pytest:
	pytest app/tests/

show_urls:
	$(manage_py) show_urls

coverage:
	pytest --cov=app app/tests/ --cov-report html && coverage report --fail-under=70.0000

show_coverage:
	python3 -c "import webbrowser; webbrowser.open('.pytest_cache/coverage/index.html')"

parse_pb_archive:
	$(manage_py) parse_privatbank_archive

gunicorn:
	cd app && gunicorn settings.wsgi:application --bind 0.0.0.0:8000 --workers 8 --log-level info --max-requests 1000 --timeout 10

gunicorn_threads:
	cd app && gunicorn settings.wsgi:application --bind 0.0.0.0:8000 --workers 8 --threads 2 --log-level info

netstat:
	netstat -tulpn|grep --color :80

grep:
	ps ax|grep 80

uwsgi_command:
	cd app && uwsgi --http :8001 --logger file:/tmp/uwsgi.log --module settings.wsgi

dokcer-compose-start:
	systemctl --user start docker-desktop

docker-compose-stop:
	systemctl --user stop docker-desktop

build_servers:
	cp -n .env.example .env && docker-compose up -d --build
