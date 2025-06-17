## Description

A future research project meant to generate high quality training data for AI models that can fix code autonomously. 

This is meant to be a tool to generate high quality synthetic data in the form of source code.

## High level overview

1. Map all CWEs to specific code examples of {vulnerable, patched} code pairs
2. Use some random high-quality LLM to generate said pairs
3. Validate pairs by hand and "approve" them for use as synthetic data
4. Use synthetic data to train high-quality secure coding models

## Project Structure

```
.
├── ephemeral-data/           # Main data directory
│   └── generated-cwes/       # CWE-specific examples
│       └── CWE-XXX/          # Individual CWE examples
│           ├── cwe-manifest.json
│           └── 1.code/       # Code examples
│               ├── code-manifest.json
│               ├── secure/     # Patched code
│               ├── vulnerable/ # Vulnerable code
│               └── payload/    # Attack payloads
├── ephemeral-data.example/  # Example data structure
└── prompts/                 # LLM prompts for generation
```

## Data Organization

Each CWE example contains:
- A manifest file `cwe-manifest.json` describing the CWE and its examples
- Code examples organized into secure, vulnerable, and payload variants
- A code manifest `code-manifest.json` describing the files and their purposes

## Developing

    python3 -m virtualenv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

## Actions

### Format code

    python3 -m black SyntheticCWEDatabase

### Run unit tests

    python3 -m unittest discover SyntheticCWEDatabase

### Run code coverage

    pytest SyntheticCWEDatabase/tests --cov --cov-branch --cov-report=xml

### Fetch CWE data

This downloads the CWE database as an XML file.

    python3 -m SyntheticCWEDatabase.fetchcwedata

## Sources

- https://arxiv.org/html/2504.16584v1#bib.bib24
- https://cwe.mitre.org/data/downloads.html
