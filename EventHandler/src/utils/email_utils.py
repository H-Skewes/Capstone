"""
Email Utility Functions
Phishing Spot - AI Phishing Agent

 reusable helper functions
for processing reported phishing emails.
"""


def normalize_email_address(address):
    """
    Remove surrounding whitespace and convert
    an email address to lowercase.
    """
    return address.strip().lower()


from html import unescape
import re

from src.models.email import Email


def extract_email(email_data):
    """
    Extract relevant email information from
    a Microsoft Graph-style email dictionary.

    Returns an Email object.
    """
    sender_info = email_data.get("from") or {}
    sender_address = (
        sender_info.get("emailAddress") or {}
    ).get("address", "")

    subject = email_data.get("subject") or ""
    message_id = email_data.get("id") or ""
    received_time = email_data.get("receivedDateTime")

    body_info = email_data.get("body") or {}
    body = body_info.get("content") or ""

    if body_info.get("contentType", "").lower() == "html":
        body = re.sub(r"<[^>]+>", " ", body)
        body = unescape(body)
        body = " ".join(body.split())

    return Email(
        message_id=message_id,
        sender=normalize_email_address(sender_address),
        subject=subject,
        body=body,
        received_time=received_time,
    )
