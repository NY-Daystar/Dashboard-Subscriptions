APP="dashboard-subscription"

.PHONY: run

run:
	flask run

run-debug:
	flask run --debug

run-external:
	flask run --host=0.0.0.0

run-console-debug:
	python . --console --debug

check_fix:
	ruff check --fix

check:
	ruff check

check_sca:
	safety check

test:
	pytest

list-modules:
	poetry show --tree

update-modules:
	poetry update

install-modules:
	poetry install

uninstall-modules:
	pip uninstall -y -r <(pip freeze)

# list all target in makefile
list:
	@grep '^[^#[:space:]].*:' Makefile | grep -v '\.PHONY'