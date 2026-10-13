"""
Configuration Settings
Phishing Spot - AI Phishing Agent

Loads configuration values from environment variables.

"""

import os


class Settings:
    """Configuration for the inbox event handler."""

    TENANT_ID = os.getenv("AZURE_TENANT_ID")
    CLIENT_ID = os.getenv("AZURE_CLIENT_ID")
    PHISHING_MAILBOX = os.getenv("PHISHING_MAILBOX")


settings = Settings()
