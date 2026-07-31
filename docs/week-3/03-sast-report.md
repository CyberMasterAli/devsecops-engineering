# SAST Scan Report

## Objective

Perform Static Application Security Testing using Bandit and analyze the identified vulnerabilities.

## Files Scanned

- vulnerable_app.py
- fixed_app.py

## Vulnerabilities Detected

The vulnerable application intentionally contained several security issues.

### 1. Hardcoded Password

Severity: Low

Description:
A password was directly stored inside the source code.

### 2. Unsafe eval()

Severity: Medium

Description:
The eval() function executes arbitrary Python expressions, allowing code injection attacks.

### 3. subprocess with shell=True

Severity: High

Description:
Using shell=True can allow command injection if user input is not properly validated.

### 4. Weak Random Number Generator

Severity: Low

Description:
The random module is not suitable for generating security-sensitive values such as passwords or OTPs.

## Report Files

- week3-bandit-report.txt
- week3-report.json

## Conclusion

Bandit successfully identified multiple security weaknesses in the vulnerable application, demonstrating the effectiveness of Static Application Security Testing.