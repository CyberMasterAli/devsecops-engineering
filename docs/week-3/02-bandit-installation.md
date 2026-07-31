# Bandit Installation

## Objective

Install and configure Bandit for performing Static Application Security Testing on the Python application.

## Installation

Install Bandit using pip.

```bash
pip install bandit
```

## Verify Installation

```bash
bandit --version
```

## Scan Entire Week 3 Source Folder

```bash
bandit -r src/week-3
```

## Generate Text Report

```bash
bandit -r src/week-3 > report/week3-bandit-report.txt
```

## Generate JSON Report

```bash
bandit -r src/week-3 -f json -o report/week3-report.json
```

## Outcome

Bandit was successfully installed and used to scan the project for security vulnerabilities.