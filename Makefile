build:
	pipenv install --dev

lint:
	pipenv check
	pipenv run flake8

test: lint
	pipenv run behave
