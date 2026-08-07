# Week 4 Software Composition Analysis Report

## Project Information

| Field | Value |
|---|---|
| Project | DevSecOps Engineering |
| Week | Week 4 |
| Application | Python Flask Web Application |
| Repository | CyberMasterAli/devsecops-engineering |
| Scanner | pip-audit |
| Report generated | 2026-08-04 09:10:10 |
| Dependency manifest | src/week-4/requirements.txt |
| SBOM | report/week4-sbom.json |

## Objectives

The objectives of this Software Composition Analysis activity were to:

* Identify direct and transitive Python dependencies.
* Scan package versions for publicly known vulnerabilities.
* Record vulnerable package versions and available fixes.
* Remediate vulnerable dependencies.
* Verify the remediated dependency set.
* Generate a CycloneDX Software Bill of Materials.
* Integrate dependency scanning into the CI/CD pipeline.

## Tools Used

* Python virtual environment
* pip
* pip-audit
* CycloneDX
* GitHub Actions
* GitHub Dependabot
* GitHub Dependency Review

## Final Dependency Inventory

| Package | Installed Version | Dependency Type |
|---|---:|---|
| blinker | 1.9.0 | Transitive |
| click | 8.4.2 | Transitive |
| colorama | 0.4.6 | Transitive |
| Flask | 3.1.3 | Direct |
| itsdangerous | 2.2.0 | Transitive |
| Jinja2 | 3.1.6 | Transitive |
| MarkupSafe | 3.0.3 | Transitive |
| Werkzeug | 3.1.8 | Transitive |
