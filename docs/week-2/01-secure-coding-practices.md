# Week 2 — Secure Coding Practices

## 1. Objective

The objective of this task was to understand and practically implement secure
coding controls. The exercise focused on preventing insecure input, avoiding
hard-coded credentials, safely handling errors, protecting sensitive output
and testing security requirements.

## 2. Secure Coding Practices Implemented

The following secure coding controls were implemented:

- Input validation through an allow-list
- Minimum and maximum input lengths
- Rejection of dangerous special characters
- Controlled exception handling
- Security-focused logging
- Secret masking
- Environment-variable configuration
- Cryptographically secure token generation
- Automated security unit tests
- Prevention of hard-coded credentials

## 3. Input Validation

The application validates usernames using a regular expression. Only letters,
numbers and underscores are accepted. The username must contain between three
and twenty characters.

Example:

```python
USERNAME_PATTERN = re.compile(r"^[A-Za-z0-9_]{3,20}$")