# Week 2 — Daily Work Log

## Project

DevSecOps Engineering Internship

## Week

Week 2

## Topics

- Secure Coding Practices
- Secret Management
- DevSecOps Automation

## Activities Completed

| Activity | Status | Evidence |
|---|---|---|
| Created Week 2 project structure | Completed | 02-week2-folder-structure.png |
| Implemented input validation | Completed | 03-secure-code-valid-input.png |
| Tested malicious input rejection | Completed | 04-invalid-input-rejected.png |
| Created automated security tests | Completed | 05-security-tests-passed.png |
| Updated `.gitignore` | Completed | 06-gitignore-secret-protection.png |
| Configured environment variable | Completed | 07-environment-secret-masked.png |
| Verified `.env` was ignored | Completed | 08-env-file-ignored.png |
| Configured GitHub Actions secret | Completed | 09-github-actions-secret-added.png |
| Created GitHub Actions workflow | Completed | 10-github-actions-workflow.png |
| Created automatic push script | Completed | 12-auto-push-script.png |
| Pushed Week 2 changes | Completed | 14-week2-commit-pushed.png |
| Executed automated workflow | Completed | 15-github-actions-run.png |
| Verified workflow success | Completed | 16-security-workflow-passed.png |

## Knowledge Gained

During Week 2, I learned that secure coding must be implemented throughout the
development process rather than added only after an application is completed.

I practiced validating user-controlled data, limiting input length, handling
errors safely, generating secure tokens and avoiding sensitive information in
logs.

I also learned that secrets should not be written directly inside application
source code. Environment variables, `.gitignore` rules and GitHub Actions
secrets were used to protect confidential values.

Finally, I implemented automation using PowerShell and GitHub Actions. The
PowerShell script reduced repetitive Git commands, while GitHub Actions
automatically validated the code after it was pushed.

## Challenges

The main challenge was ensuring that local secret files remained available for
development but were not uploaded to GitHub. This was resolved using
`.gitignore`, `.env.example` and the `git check-ignore` command.

## Final Result

All planned Week 2 tasks were completed successfully. The repository now
contains a secure coding demonstration, security tests, secret-management
controls and automated GitHub security checks.