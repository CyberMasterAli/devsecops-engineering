# Week 2 — Secret Management

## 1. Objective

The objective of this task was to prevent API keys, passwords, access tokens and
other credentials from being stored directly in source code or uploaded to
GitHub.

## 2. What Is a Secret?

A secret is confidential information used by an application or automation
process.

Examples include:

- API keys
- Access tokens
- Database passwords
- Private keys
- Cloud credentials
- Deployment credentials
- Encryption keys

## 3. Risks of Hard-Coded Secrets

Hard-coded secrets can be exposed through:

- Public GitHub repositories
- Git history
- Screenshots
- Application logs
- Shared source-code archives
- Build output
- Configuration files

Deleting a secret from the latest source file does not automatically remove it
from older Git commits.

## 4. Controls Implemented

The following controls were implemented:

- Added `.env` files to `.gitignore`
- Created a safe `.env.example` template
- Stored local secrets in environment variables
- Masked secrets before displaying them
- Created a GitHub Actions repository secret
- Added workflow checks for prohibited secret files
- Added checks for common hard-coded credential patterns

## 5. Local Environment Variables

The demonstration API key was configured temporarily in PowerShell:

```powershell
$env:DEVSECOPS_API_KEY = "temporary-demo-value"