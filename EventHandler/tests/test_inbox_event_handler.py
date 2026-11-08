"""
Inbox Event Handler Tests
Phishing Spot - AI Phishing Agent

This file will contain tests for the inbox event handler.

Planned Tests:
1. Incoming events are received correctly.
2. Reported email IDs are identified.
3. Invalid events are handled appropriately.
4. Email information is passed to the next component.
"""


def test_placeholder():
    """Verify that the initial test setup works."""
    assert True



import json
import unittest
from pathlib import Path

from src.utils.email_utils import extract_email


class TestEmailExtraction(unittest.TestCase):

    def test_mock_phishing_email(self):
        mock_file = (
            Path(__file__).parent
            / "mock_phishing_email.json"
        )

        with open(mock_file, "r", encoding="utf-8") as file:
            email_data = json.load(file)

        result = extract_email(email_data)

        self.assertEqual(
            result.message_id,
            "mock-phishing-001"
        )

        self.assertEqual(
            result.sender,
            "it-support@fake-company.example"
        )

        self.assertEqual(
            result.subject,
            "URGENT: Your Account Will Be Disabled"
        )

        self.assertIn(
            "verify your login",
            result.body
        )

        self.assertEqual(
            result.received_time,
            "2026-11-07T14:30:00Z"
        )
