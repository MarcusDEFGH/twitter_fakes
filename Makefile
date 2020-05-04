# Makefile

clean: clean-build clean-pyc clean-test clean-docker

clean-build:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr .eggs/
	@find . -name '*.egg-info' -exec rm -fr {} +
	@find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	@rm -fr .tox/
	@rm -f .coverage
	@rm -fr htmlcov/

clean-docker:
	@docker system prune --volumes --force

check.test_path:
	@if test "$(TEST_PATH)" = "" ; then echo "TEST_PATH is undefined. The default is tests."; fi

test: check.test_path
	@py.test $(TEST_PATH) --cov --cov-report term-missing --basetemp=tests/media --disable-pytest-warnings

test.failfirst: check.test_path
	@py.test -x $(TEST_PATH) --cov-report term-missing --basetemp=tests/media --disable-pytest-warnings

test.collect: check.test_path
	@py.test $(TEST_PATH) --collect-only --disable-pytest-warnings

### UTIL

shell: check.settings
	@docker-compose run --rm webserver python manage.py shell

### DATABASE

mig:
	@docker-compose run --rm webserver python manage.py migrate --noinput

mig.check:
	@docker-compose run --rm webserver python manage.py migrate --list

mig.list:
	@find . -path "*/migrations/*.py"

makemig:
	@docker-compose run --rm webserver python manage.py makemigrations 
 
### DOCKER

build:
	@docker-compose build

build.nocache:
	@docker-compose build --no-cache
 
start:
	@docker-compose -f docker-compose.yml up -d
 
stop:
	@docker-compose stop
 
restart:
	@make -s stop
	@make -s start
