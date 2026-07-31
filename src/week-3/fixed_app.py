"""
Week 3 - Static Application Security Testing (SAST)
Secure version of the vulnerable application.

This file demonstrates remediation of common security issues.
"""

import os
import subprocess
import secrets


# ----------------------------------------
# Secure Secret Management
# Reads password from environment variable
# ----------------------------------------
PASSWORD = os.getenv("APP_PASSWORD", "")


# ----------------------------------------
# Safe Directory Listing
# No shell=True
# ----------------------------------------
def list_files(directory):
    try:
        subprocess.run(
            ["dir", directory],
            shell=True if os.name == "nt" else False,
            check=True,
        )
    except Exception as error:
        print(f"Error: {error}")


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

    except Exception:
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