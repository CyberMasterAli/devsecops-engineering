# DevSecOps Engineering

## Internship Information

- **Organization:** Yumaj Enterprises
- **Intern:** Muhammad Ali
- **Project:** DevSecOps Engineering
- **Week:** 1
- **Assigned Activities:** Secure SDLC and Git & GitHub

## Project Objective

The objective of this project is to integrate security into the software
development lifecycle through secure development practices, version control,
security testing, and secure CI/CD practices.

## Week 1 Objectives

The objectives of Week 1 are:

- Understand the Software Development Life Cycle.
- Understand the Secure Software Development Life Cycle.
- Identify security activities for each SDLC phase.
- Create initial security requirements.
- Create an initial cybersecurity risk register.
- Create a basic threat model.
- Define security gates.
- Configure Git.
- Create and manage a GitHub repository.
- Demonstrate commits, branches, pull requests, and change tracking.

## Week 1 Documents

- [Secure SDLC](docs/week-1/01-secure-sdlc.md)
- [Security Requirements](docs/week-1/02-security-requirements.md)
- [Risk Register](docs/week-1/03-risk-register.md)
- [Threat Model](docs/week-1/04-threat-model.md)
- [Security Gates](docs/week-1/05-security-gates.md)
- [Daily Work Log](docs/week-1/06-daily-work-log.md)

## Git Workflow

```mermaid
flowchart LR
    A[Local Files] --> B[Git Status]
    B --> C[Git Add]
    C --> D[Git Commit]
    D --> E[Feature Branch]
    E --> F[Git Push]
    F --> G[Pull Request]
    G --> H[Review]
    H --> I[Merge into Main]




    ## Week 2 — Secure Coding, Secret Management and Automation

Week 2 focuses on integrating security controls into source code and the
development workflow.

### Completed Tasks

- Implemented input validation
- Added secure exception handling
- Generated cryptographically secure tokens
- Loaded credentials from environment variables
- Protected `.env` and credential files through `.gitignore`
- Configured a GitHub Actions repository secret
- Added automated security unit tests
- Created a GitHub Actions security workflow
- Created a PowerShell Git automation script

### Week 2 Files

- `docs/week-2/01-secure-coding-practices.md`
- `docs/week-2/02-secret-management.md`
- `docs/week-2/03-automation.md`
- `docs/week-2/04-daily-work-log.md`
- `src/week-2/secure_app.py`
- `src/week-2/test_secure_app.py`
- `.github/workflows/security-check.yml`
- `scripts/auto-push.ps1`