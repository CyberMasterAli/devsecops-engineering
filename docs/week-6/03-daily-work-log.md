# Daily Work Log - Week 6

**Date:** August 21, 2026
**Name:** Zain
**Role:** DevSecOps Engineering Intern

## Tasks Completed Today:
1. **Environment Configuration:** Set up the Week 6 directory structure, created branch `week-6-container-security`, and successfully installed/configured Docker Desktop with WSL 2.
2. **Container Security Basics:** Wrote a secure `Dockerfile` for the Python application, implementing best practices such as an alpine base image, a non-root user, and a `.dockerignore` file.
3. **Local Image Scanning:** Built the Docker image and executed a local Trivy vulnerability scan, capturing the output for the project report.
4. **CI/CD Pipeline Security:** Authored a GitHub Actions workflow to automate Trivy scanning on all pushes and pull requests to the `main` branch.
5. **Documentation:** Updated the required markdown files in the `docs` directory detailing container security and image scanning procedures.

## Challenges Faced:
- **Issue:** The `docker` command was initially unrecognized in the PowerShell terminal.
- **Resolution:** Installed Docker Desktop, ensured the WSL 2 backend was selected, and launched a fresh PowerShell session to reload the system environment paths.

## Next Steps:
- Push the final commits to GitHub.
- Verify the successful execution of the GitHub Actions Trivy scan.
- Merge the Pull Request into the `main` branch.