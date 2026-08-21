# Image Scanning with Trivy

Implemented container image scanning to detect Common Vulnerabilities and Exposures (CVEs) in both OS packages and application dependencies.

- **Local Scanning:** Utilized Trivy via the Docker CLI (`aquasec/trivy`) to analyze the local image. The vulnerability output was exported and saved to `report/week6-trivy-report.txt`.
- **CI/CD Automation:** Integrated the `trivy-action` tool into GitHub Actions (`week6-container-scan.yml`). 
- **Security Gate:** The pipeline is strictly configured to fail (`exit-code: 1`) and block pull requests if any `CRITICAL` or `HIGH` vulnerabilities are detected in the image build.