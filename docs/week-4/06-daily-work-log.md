# Week 4 Daily Work Log

## Project Information

| Field | Value |
|---|---|
| Project | DevSecOps Engineering |
| Week | Week 4 |
| Topic | Dependency Scanning and Software Composition Analysis |
| Application | Python Flask Web Application |

## Daily Activities

| Day | Date | Activity | Result |
|---|---|---|---|
| Day 1 | [ACTUAL DATE] | Studied dependency scanning and Software Composition Analysis | Concepts and objectives documented |
| Day 2 | [ACTUAL DATE] | Created Week 4 project directories and installed pip-audit | Scanner installed successfully |
| Day 3 | [ACTUAL DATE] | Created a controlled vulnerable dependency manifest and performed the initial scan | Known vulnerabilities detected and recorded |
| Day 4 | [ACTUAL DATE] | Generated text and JSON vulnerability reports | Initial scan evidence preserved |
| Day 5 | [ACTUAL DATE] | Created the Python Flask web application | Root and health endpoints tested |
| Day 6 | [ACTUAL DATE] | Installed current compatible dependencies and generated requirements.txt | Final dependency inventory created |
| Day 7 | [ACTUAL DATE] | Performed the remediated dependency scan | Final scan result recorded |
| Day 8 | [ACTUAL DATE] | Generated the Software Composition Analysis report and CycloneDX SBOM | SCA artifacts generated |
| Day 9 | [ACTUAL DATE] | Created GitHub Actions dependency scanning and Dependency Review workflows | CI/CD security controls added |
| Day 10 | [ACTUAL DATE] | Configured Dependabot and pushed Week 4 work to GitHub | Automated dependency monitoring enabled |

## Work Summary

During Week 4, dependency scanning and Software Composition Analysis were
implemented for a Python Flask web application.

The work included:

- Installing and configuring `pip-audit`.
- Scanning a controlled outdated dependency.
- Recording vulnerability identifiers and remediation information.
- Creating a secure Flask application.
- Installing and pinning current dependencies.
- Verifying the remediated dependency set.
- Generating text, JSON, Markdown, and CycloneDX reports.
- Adding GitHub Actions dependency scanning.
- Adding pull-request dependency review.
- Configuring Dependabot.
- Recording screenshots as project evidence.

## Challenges Encountered

During report generation, some output files were not created automatically
when the scan returned no vulnerability findings.

The issue was resolved by:

- Verifying that required input files existed.
- Checking command exit codes.
- Separating standard output and error output.
- Validating generated JSON files.
- Creating the final Markdown SCA report from the real dependency inventory
  and scan results.

## Final Outcome

Week 4 successfully demonstrated how dependency scanning and Software
Composition Analysis can be integrated into a DevSecOps workflow.

The project now contains:

- A Python Flask web application
- A fully pinned dependency manifest
- Vulnerability scan reports
- A CycloneDX SBOM
- GitHub Actions security workflows
- Dependabot configuration
- Documentation and screenshot evidence