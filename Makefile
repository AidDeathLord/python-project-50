install:
	poetry install
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python -m pip install --user dist/*.whl
package-reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl
lint:
	poetry run flake8 gen_diff

run-gendiff:
	poetry run gendiff -h