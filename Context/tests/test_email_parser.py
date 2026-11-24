import pytest

from src.email_parser import parse_email

def test_valid_email():
    email = {
        "sender": "security@example.com",
        "subject": "Verify your account",
        "body": "Please verify your password immediately.",
        "message_id": "12345",
        "timestamp": "2026-11-22 14:30:00"
    }

    result = parse_email(email)
    assert result == email


def test_missing_subject():
    email = {
        "sender": "user@example.com",
        "body": "hello",
        "message_id": "12345",
        "timestamp": "2026-11-22 14:30:00"
    }
    result = parse_email(email)

    assert result ["subject"] == ""

def test_missing_sender():
    email = {
        "subject": "Account Alert",
        "body": "Verify your account.",
        "message_id": "12345",
        "timestamp": "2026-11-22 14:30:00"
    }

    with pytest.raises(ValueError, match="Sender cannot be empty"):
        parse_email(email)


def test_invalid_input():
    with pytest.raises(ValueError, match="Email data must be a dictionary"):
        parse_email("Invalid email")


def test_missing_body():
    email = {
        "sender": "user@example.com",
        "subject": "Hello",
        "message_id": "12345",
        "timestamp": "2026-11-22 14:30:00"
    }

    result = parse_email(email)

    assert result["body"] == ""