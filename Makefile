# Variables
PYTEST = pytest
COVERAGE = --cov=.
TEST_TARGETS = $(shell find . -name "*.py" ! -path "./venv/*")
RUFF = ruff
RUFF_OPTS = --fix
LINTING_DEST = .

# Targets
default: lint test clean

lint:
	@echo "Linting code with Ruff"
	$(RUFF) $(RUFF_OPTS) $(LINTING_DEST)
	@echo " "

test:
	@echo "Running tests with coverage"
	$(PYTEST) $(COVERAGE) $(TEST_TARGETS)
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