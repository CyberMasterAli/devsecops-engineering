# Week 2 — DevSecOps Automation

## 1. Objective

The objective of this task was to automate repetitive Git and security
validation operations.

Two forms of automation were implemented:

1. Local Git automation using PowerShell
2. Continuous security validation using GitHub Actions

## 2. Local Git Automation

The `scripts/auto-push.ps1` script automates:

```text
Review changes
→ Stage files
→ Create commit
→ Push branch to GitHub