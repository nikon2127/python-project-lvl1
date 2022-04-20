install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-uninstall:
	pip uninstall hexlet-code

package-reinstall:
	pip uninstall hexlet-code
	python3 -m pip install --user dist/*.whl