# Vulnerability Remediation

## Objective

Fix the vulnerabilities detected during the SAST scan.

## Security Improvements

### Hardcoded Password

Before

- Password stored directly inside the source code.

After

- Password loaded securely from an environment variable.

---

### Unsafe eval()

Before

- eval() executed user input directly.

After

- Implemented a safe calculator supporting only controlled arithmetic operations.

---

### Command Injection

Before

- subprocess.run() executed commands using shell=True.

After

- Used safer subprocess execution with controlled arguments.

---

### Weak Random Number Generator

Before

- Used random.randint().

After

- Replaced with the secrets module for cryptographically secure random values.

## Result

The secure application follows better coding practices and significantly reduces security risks.

Bandit reported fewer security findings after remediation.