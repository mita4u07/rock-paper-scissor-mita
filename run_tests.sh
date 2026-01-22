#!/bin/bash
# Test runner script for Rock-Paper-Scissors-Lizard-Spock game

echo "Running unit tests with coverage..."
python -m pytest test_main.py -v --cov=main --cov-report=term-missing --cov-report=html

echo ""
echo "Coverage report generated in htmlcov/index.html"
