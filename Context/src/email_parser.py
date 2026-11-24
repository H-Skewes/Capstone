
def parse_email(email_data):
    """
    Receives email from email extractors, then retturns a distionary for the context builder.
    """

    if not isinstance(email_data, dict):
        raise ValueError("Email data must be a dictionary.")

    required_fields = [
        "sender",
        "subject",
        "body",
        "message_id",
        "timestamp"
    ]

    parsed_email = {}

    for field in required_fields:
        value = email_data.get(field)

        if value is None:
            parsed_email[field] = ""
        elif isinstance(value, str):
            parsed_email[field] = value.strip()
        else:
            raise ValueError(f"Invalid data type for {field}")

    if not parsed_email["sender"]:
        raise ValueError("Sender cannot be empty.")

    if not parsed_email["message_id"]:
        raise ValueError("Message ID cannot be empty.")

    return parsed_email
