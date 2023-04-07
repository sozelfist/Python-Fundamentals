# Variables
PYTEST = pytest
COVERAGE = --cov=. 
SOURCES = $(shell find . -name "*.py" ! -path "./venv/*")
RUFF = ruff

# Targets
default: lint test clean

lint:
	@echo "Linting code with Ruff"
	$(RUFF) .
	@echo " "

test:
	@echo "Running tests with coverage"
	$(PYTEST) $(COVERAGE) $(SOURCES)
	@echo " "

clean:
	@echo "Removing .pytest_cache folder"
	@rm -rf .pytest_cache
	@echo "Removing .coverage file"
	@rm -f .coverage
	@echo "Removing __pycache__ folders except in .venv"
	@find . -name '__pycache__' -type d ! -path './venv/*' -exec rm -rf {} +
	@echo "Removing .ruff_cache folder"
	@rm -rf .ruff_cache