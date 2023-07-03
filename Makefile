PYTHON_FILE_PATHS = `(find . -iname "*.py" -not -path "./.venv/*")`

install: ## Install dependencies
	poetry install

hard-install: ## Clear and install dependencies
	rm -rf .venv & make install

lab: ## Launch Jupyterlab instance
	poetry run jupyter-lab

lab-kernel: ## Create jupyter-lab kernel
	poetry run jupyter kernelspec uninstall comsim-core
	poetry run ipython kernel install --name "comsim-core" --user

requirements-export: ## Export production requirements
	poetry export -f requirements.txt --output requirements.txt --without-hashes

requirements-export-all: ## Export development and production requirements
	poetry export --dev -f requirements.txt --output requirements.txt --without-hashes

pylint: ## Run Pylint
	poetry run pylint -s no --rcfile=.pylintrc $(PYTHON_FILE_PATHS)

isort: ## Run Isort
	poetry run isort --check-only $(PYTHON_FILE_PATHS)

isort-fix: ## Run Isort with automated fix
	poetry run isort $(PYTHON_FILE_PATHS)

black: ## Run Black
	poetry run black --check --quiet $(PYTHON_FILE_PATHS)

black-fix: ## Run Black with automated fix
	poetry run black $(PYTHON_FILE_PATHS)

pytest: ## Run Pytest
	poetry run pytest tests/

pytest-coverage: ## Run coverage report
	poetry run coverage run -m pytest tests/
	poetry run coverage report

pack circles: ## Run packing of cricles on Square Domain
	poetry run python src/core/decomposition/main.py

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-25s\033[0m %s\n", $$1, $$2}'
