# Static Application Security Testing (SAST)

## Objective

The objective of this task is to learn and implement Static Application Security Testing (SAST) as part of the DevSecOps software development lifecycle.

## What is SAST?

Static Application Security Testing (SAST) is a security testing technique that analyzes an application's source code, bytecode, or binaries without executing the program. It identifies security vulnerabilities early in the Software Development Life Cycle (SDLC), allowing developers to fix issues before deployment.

## Benefits of SAST

- Detects vulnerabilities during development.
- Improves software security.
- Reduces the cost of fixing security issues.
- Integrates easily into CI/CD pipelines.
- Supports secure coding practices.

## Common Vulnerabilities Detected

- Hardcoded credentials
- Command Injection
- SQL Injection
- Cross-Site Scripting (XSS)
- Unsafe function usage
- Weak cryptography
- Insecure random number generation

## Tool Used

Bandit

Bandit is an open-source Static Application Security Testing tool specifically designed for Python applications. It scans Python source code for common security issues and provides detailed reports.