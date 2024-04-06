# Variables
PYTEST = pytest
COVERAGE = --cov=.
TEST_TARGETS = $(shell find . -name "*.py" ! -path "./venv/*")
RUFF = ruff
RUFF_CHECK_OPTS = check
RUFF_OPTS = --fix
LINTING_DEST = .

# Targets
.PHONY: default lint test clean

default: lint test clean

lint:
	@echo "Linting code with Ruff"
	@$(RUFF) $(RUFF_CHECK_OPTS) $(LINTING_DEST)
	@echo " "

test:
	@echo "Running tests with coverage"
	@$(PYTEST) $(COVERAGE) $(TEST_TARGETS)
	@echo " "

clean:
	@echo "Removing temporary files and folders"
	@rm -rf .pytest_cache
	@rm -f .coverage
	@find . -name '__pycache__' -type d ! -path './venv/*' -exec rm -rf {} +
	@rm -rf .ruff_cache
	@echo "Cleanup completed"
