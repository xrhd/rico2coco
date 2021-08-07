install:
	poetry install

test: format
test:
	pytest . $(PYTEST_OPTIONS)

format:
	isort rico2coco tests
	black rico2coco tests
