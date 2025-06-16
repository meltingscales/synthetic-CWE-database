## Description

A future research project meant to generate high quality training data for AI models that can fix code autonomously. 

This is meant to be a tool to generate high quality synthetic data in the form of source code.

## High level overview

1. Map all CWEs to specific code examples of {vulnerable, patched} code pairs
2. Use some random high-quality LLM to generate said pairs
3. Validate pairs by hand and "approve" them for use as synthetic data
4. Use synthetic data to train high-quality secure coding models

## Sources

- https://arxiv.org/html/2504.16584v1#bib.bib24
- https://cwe.mitre.org/data/downloads.html
