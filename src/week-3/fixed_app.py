"""
Week 3 - Static Application Security Testing (SAST)
Secure version of the vulnerable application.

This file demonstrates remediation of common security issues.
"""

import os
import subprocess
import secrets
import logging


logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)


# ----------------------------------------
# Secure Secret Management
# Reads password from environment variable
# ----------------------------------------
PASSWORD = os.getenv("APP_PASSWORD", "")


# ----------------------------------------
# Safe Directory Listing
# No shell=True - prevents command injection
# ----------------------------------------
def list_files(directory):
    try:
        if os.name == "nt":
            subprocess.run(
                ["cmd", "/c", "dir", directory],
                shell=False,
                check=True,
            )
        else:
            subprocess.run(
                ["ls", "-la", directory],
                shell=False,
                check=True,
            )
    except subprocess.CalledProcessError as error:
        logger.error(f"Error listing files: {error}")
    except ValueError as error:
        logger.error(f"Invalid directory: {error}")


# ----------------------------------------
# Safe Calculator
# Only integer addition is allowed
# Example: 5+10
# ----------------------------------------
def calculate(expression):
    try:
        parts = expression.split("+")

        if len(parts) != 2:
            raise ValueError("Only addition is allowed (example: 5+10).")

        first = int(parts[0].strip())
        second = int(parts[1].strip())

        return first + second

    except (ValueError, AttributeError) as error:
        logger.error(f"Calculation error: {error}")
        return "Invalid Expression"


# ----------------------------------------
# Cryptographically Secure OTP
# ----------------------------------------
def generate_otp():
    return secrets.randbelow(900000) + 100000


# ----------------------------------------
# Main Program
# ----------------------------------------
def main():

    print("=== Secure Application ===")

    folder = input("Enter directory name: ")
    list_files(folder)

    expression = input("Enter expression (Example: 5+10): ")
    print("Result:", calculate(expression))

    print("Generated OTP:", generate_otp())

    if PASSWORD:
        print("Password loaded securely from environment variable.")
    else:
        print("APP_PASSWORD environment variable is not set.")


if __name__ == "__main__":
    main()
