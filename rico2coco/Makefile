install:
	poetry install

test: format
test:
	pytest . $(PYTEST_OPTIONS)

format:
	isort .
	black .
