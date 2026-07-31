# GitHub Actions SAST Integration

## Objective

Automate Static Application Security Testing using GitHub Actions.

## Workflow File

.github/workflows/sast.yml

## Workflow Process

1. Checkout repository.
2. Install Python.
3. Install Bandit.
4. Scan the source code.
5. Display the scan results.

## Benefits

- Automated security scanning
- Continuous Integration
- Early vulnerability detection
- Consistent security checks
- Faster developer feedback

## Outcome

Every push to the GitHub repository automatically triggers a Bandit scan, ensuring continuous security testing throughout development.