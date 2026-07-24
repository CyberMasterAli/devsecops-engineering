"""Security tests for the Week 2 secure coding demonstration."""

import os
import unittest
from unittest.mock import patch

from secure_app import (
    generate_secure_token,
    get_api_key,
    mask_secret,
    process_user,
    validate_comment,
    validate_username,
)


class SecureAppTests(unittest.TestCase):
    def test_valid_username(self) -> None:
        self.assertTrue(validate_username("CyberMaster_01"))

    def test_username_with_spaces_is_rejected(self) -> None:
        self.assertFalse(validate_username("Cyber Master"))

    def test_username_with_special_characters_is_rejected(self) -> None:
        self.assertFalse(validate_username("admin<script>"))

    def test_short_username_is_rejected(self) -> None:
        self.assertFalse(validate_username("ab"))

    def test_valid_comment(self) -> None:
        self.assertTrue(validate_comment("Secure coding completed."))

    def test_empty_comment_is_rejected(self) -> None:
        self.assertFalse(validate_comment("   "))

    def test_long_comment_is_rejected(self) -> None:
        self.assertFalse(validate_comment("A" * 201))

    def test_valid_user_is_processed(self) -> None:
        result = process_user("intern_user", "Week 2 completed")

        self.assertEqual(result["status"], "accepted")
        self.assertEqual(result["username"], "intern_user")

    def test_invalid_user_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            process_user("../administrator", "Invalid username test")

    def test_secret_is_masked(self) -> None:
        masked_value = mask_secret("super-secret-api-key")

        self.assertNotEqual(masked_value, "super-secret-api-key")
        self.assertIn("*", masked_value)

    def test_secure_tokens_are_unique(self) -> None:
        first_token = generate_secure_token()
        second_token = generate_secure_token()

        self.assertNotEqual(first_token, second_token)
        self.assertGreater(len(first_token), 20)

    @patch.dict(os.environ, {"DEVSECOPS_API_KEY": "test-secret-key"})
    def test_api_key_from_environment(self) -> None:
        self.assertEqual(get_api_key(), "test-secret-key")

    @patch.dict(os.environ, {}, clear=True)
    def test_missing_api_key(self) -> None:
        with self.assertRaises(RuntimeError):
            get_api_key()


if __name__ == "__main__":
    unittest.main()