#!/usr/bin/zsh

echo "Running tests with coverage..."
pytest --cov=$(find . -name "*.py" ! -path "./venv/*")

echo "Removing .pytest_cache folder..."
rm -rf .pytest_cache

echo "Removing .coverage file..."
rm .coverage

echo "Removing __pycache__ folders except in .venv..."
find . -name __pycache__ -type d ! -path "./.venv/*" -exec rm -rf {} +
