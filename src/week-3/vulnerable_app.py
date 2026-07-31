"""
Week 3 - Static Application Security Testing (SAST)
Intentionally vulnerable Python application for Bandit scanning.

NOTE:
This file is intentionally insecure for educational purposes only.
"""

import subprocess
import random


# -------------------------------
# Hardcoded Secret (Bandit: B105)
# -------------------------------
PASSWORD = "Admin@123"


# ---------------------------------------
# Unsafe Command Execution (Bandit: B602)
# ---------------------------------------
def list_files(user_input):
    command = "dir " + user_input
    subprocess.run(command, shell=True)


# --------------------------
# Dangerous eval() (B307)
# --------------------------
def calculate(expression):
    return eval(expression)


# ---------------------------------
# Weak Random Number (Bandit: B311)
# ---------------------------------
def generate_otp():
    return random.randint(100000, 999999)


# --------------------
# Main Program
# --------------------
def main():
    print("=== Vulnerable Application ===")

    folder = input("Enter folder name: ")
    list_files(folder)

    expr = input("Enter calculation: ")
    print("Result:", calculate(expr))

    print("Generated OTP:", generate_otp())

    if PASSWORD == "Admin@123":
        print("Login Successful")


if __name__ == "__main__":
    main()
    