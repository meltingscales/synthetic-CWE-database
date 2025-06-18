# List available commands
default:
    @just --list

# Install dependencies
install:
    pip install -r requirements.txt

# Run tests
test:
    pytest SyntheticCWEDatabase/tests

# Run tests with coverage
test-cov:
    pytest SyntheticCWEDatabase/tests --cov --cov-branch --cov-report=term-missing

# Run tests with dummy AI
test-dummy-ai:
    USE_DUMMY_AI=true pytest SyntheticCWEDatabase/tests

# Download CWE data
fetch-cwe:
    python3 -m SyntheticCWEDatabase.fetchcwedata

# Generate code examples for a specific CWE
generate-cwe cwe_id="79" language="python":
    python3 -m SyntheticCWEDatabase --generate-data --cwe-id {{cwe_id}} --language {{language}}

# Clean up generated files
clean:
    python3 -m SyntheticCWEDatabase --destroy-generated-data

# Format code
fmt:
    black SyntheticCWEDatabase/

# Lint code
lint:
    flake8 SyntheticCWEDatabase/
    mypy SyntheticCWEDatabase/

# Run all checks
check: fmt lint test 