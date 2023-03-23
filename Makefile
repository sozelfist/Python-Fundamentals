# Variables
PYTEST = pytest
COVERAGE = --cov=$(shell find . -name "*.py" ! -path "./venv/*")
FLAKE8 = flake8

# Targets
default: lint test clean

lint:
	@echo "Linting code with Flake8..."
	$(FLAKE8) .
	@echo "********************************************************************"

test:
	@echo "Running tests with coverage..."
	$(PYTEST) $(COVERAGE)
	@echo "********************************************************************"

clean:
	@echo "Removing .pytest_cache folder..."
	@rm -rf .pytest_cache
	@echo "Removing .coverage file..."
	@rm -f .coverage
	@echo "Removing __pycache__ folders except in .venv..."
	@find . -name '__pycache__' -type d ! -path './.venv/*' -exec rm -rf {} +
