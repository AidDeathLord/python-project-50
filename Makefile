install:
	poetry install
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install dist/*.whl
package-reinstall:
	python3 -m pip install --force-reinstall dist/*.whl
lint:
	poetry run flake8 gendiff
test:
	poetry run pytest --cov-report term-missing --cov -vv
selfcheck:
	poetry check
test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
check: selfcheck test lint
