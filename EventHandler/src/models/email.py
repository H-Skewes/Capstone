"""
Email Data Model
Phishing Spot - AI Phishing Agent

Defines the structure of a reported phishing email.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Email:
    message_id: str
    sender: str
    subject: str
    body: str
    received_time: Optional[str] = None
