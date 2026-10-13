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
