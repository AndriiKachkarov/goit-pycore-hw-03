import re


def normalize_phone(phone_number: str) -> str:
    """
    Normalizes a phone number to the standard international format for Ukraine.
    """
    cleaned = re.sub(r"[^\d+]", "", phone_number.strip())

    if cleaned.startswith("+380"):
        return cleaned
    elif cleaned.startswith("380"):
        return "+" + cleaned
    elif cleaned.startswith("0"):
        return "+38" + cleaned
    else:
        raise ValueError("Invalid phone number format")
