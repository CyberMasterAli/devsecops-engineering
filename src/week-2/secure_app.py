"""Secure coding demonstration for DevSecOps Week 2."""

import logging
import os
import re
import secrets
from typing import Final


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

USERNAME_PATTERN: Final = re.compile(r"^[A-Za-z0-9_]{3,20}$")
MAX_COMMENT_LENGTH: Final = 200


def validate_username(username: str) -> bool:
    """
    Validate a username using an allow-list.

    Valid usernames:
    - Contain letters, numbers or underscores
    - Have a length between 3 and 20 characters
    """
    if not isinstance(username, str):
        return False

    return bool(USERNAME_PATTERN.fullmatch(username))


def validate_comment(comment: str) -> bool:
    """Reject empty or excessively long comments."""
    if not isinstance(comment, str):
        return False

    cleaned_comment = comment.strip()

    return 1 <= len(cleaned_comment) <= MAX_COMMENT_LENGTH


def mask_secret(secret_value: str) -> str:
    """Prevent secrets from being printed completely."""
    if not secret_value:
        return "[NOT CONFIGURED]"

    if len(secret_value) <= 4:
        return "****"

    return f"{secret_value[:2]}{'*' * (len(secret_value) - 4)}{secret_value[-2:]}"


def generate_secure_token() -> str:
    """Generate a cryptographically secure random token."""
    return secrets.token_urlsafe(32)


def get_api_key() -> str:
    """
    Read the API key from an environment variable.

    The secret is not hard-coded in the source code.
    """
    api_key = os.getenv("DEVSECOPS_API_KEY")

    if not api_key:
        raise RuntimeError(
            "DEVSECOPS_API_KEY environment variable is not configured."
        )

    return api_key


def process_user(username: str, comment: str) -> dict[str, str]:
    """Validate user-controlled input before processing it."""
    if not validate_username(username):
        logging.warning("Rejected an invalid username.")
        raise ValueError("Username contains invalid characters or length.")

    if not validate_comment(comment):
        logging.warning("Rejected an invalid comment.")
        raise ValueError("Comment is empty or exceeds the allowed length.")

    logging.info("Validated input for user: %s", username)

    return {
        "username": username,
        "comment": comment.strip(),
        "status": "accepted",
    }


def main() -> None:
    """Run the secure coding demonstration."""
    try:
        username = input("Enter username: ").strip()
        comment = input("Enter comment: ").strip()

        result = process_user(username, comment)

        print("\nInput accepted securely:")
        print(result)

        print("\nGenerated secure session token:")
        print(generate_secure_token())

        try:
            api_key = get_api_key()
            print("\nConfigured API key:")
            print(mask_secret(api_key))
        except RuntimeError as error:
            logging.error("%s", error)

    except ValueError as error:
        logging.error("Validation error: %s", error)
    except KeyboardInterrupt:
        logging.info("Program stopped by the user.")
    except Exception:
        logging.exception("An unexpected error occurred.")


if __name__ == "__main__":
    main()