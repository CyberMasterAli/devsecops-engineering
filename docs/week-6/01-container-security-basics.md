# Container Security Basics

Implemented a secure Docker environment for the Python application to reduce the attack surface and enforce secure defaults.

- **Base Image:** Utilized `python:3.10-alpine` to minimize the attack surface by avoiding full OS distributions.
- **Least Privilege:** Created a dedicated `appuser` and `appgroup` to ensure the container does not run as the root user.
- **Data Leakage Prevention:** Implemented a `.dockerignore` file to prevent secrets, environment variables, and Git history from entering the build context.
- **Network Security:** Exposed non-privileged port `8080` instead of port `80`.