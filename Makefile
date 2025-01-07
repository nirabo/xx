.PHONY: help install dev clean lint test coverage build publish docs venv

# Variables
PYTHON := python3
VENV := venv
PIP := $(VENV)/bin/pip
PYTEST := $(VENV)/bin/pytest
BLACK := $(VENV)/bin/black
ISORT := $(VENV)/bin/isort
MYPY := $(VENV)/bin/mypy
PACKAGE_NAME := xx-cli
SRC_DIR := src/xx
TEST_DIR := tests

help:  ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

venv:  ## Create virtual environment if it doesn't exist
	test -d $(VENV) || $(PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip

install: venv  ## Install package and dependencies
	$(PIP) install -e .

dev: venv  ## Install development dependencies
	$(PIP) install -e ".[dev]"

clean:  ## Clean up build artifacts and cache
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf htmlcov
	rm -rf .mypy_cache
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete

lint: dev  ## Run code linting
	$(BLACK) $(SRC_DIR) $(TEST_DIR)
	$(ISORT) $(SRC_DIR) $(TEST_DIR)
	$(MYPY) $(SRC_DIR)

format: dev  ## Format code using black and isort
	$(BLACK) $(SRC_DIR) $(TEST_DIR)
	$(ISORT) $(SRC_DIR) $(TEST_DIR)

test: dev  ## Run tests
	$(PYTEST) $(TEST_DIR) -v

coverage: dev  ## Run tests with coverage report
	$(PYTEST) --cov=$(SRC_DIR) --cov-report=html --cov-report=term-missing $(TEST_DIR)

build: clean  ## Build package
	$(PYTHON) -m build

publish: build  ## Publish package to PyPI
	$(PYTHON) -m twine upload dist/*

publish-test: build  ## Publish package to TestPyPI
	$(PYTHON) -m twine upload --repository testpypi dist/*

docs:  ## Generate documentation
	cd docs && $(MAKE) html

watch-test: dev  ## Run tests continuously
	$(PYTEST) $(TEST_DIR) -f

check: lint test  ## Run all checks (lint and test)

init: clean install dev  ## Initialize development environment
	@echo "Creating git hooks..."
	@mkdir -p .git/hooks
	@echo '#!/bin/sh\nmake lint test' > .git/hooks/pre-commit
	@chmod +x .git/hooks/pre-commit
	@echo "Development environment initialized!"

run:  ## Run the application
	$(PYTHON) -m xx.cli.main

docker-build:  ## Build Docker image
	docker build -t $(PACKAGE_NAME) .

docker-run:  ## Run Docker container
	docker run -it --rm $(PACKAGE_NAME)

# Default target
.DEFAULT_GOAL := help