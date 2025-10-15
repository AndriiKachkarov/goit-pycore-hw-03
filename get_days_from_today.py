from datetime import datetime
from typing import Optional


def get_days_from_today(date: str) -> Optional[int]:
    """
    Calculates the number of days from today to the given date.
    If the date format is invalid, returns None.
    """
    try:
        target_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()

        delta = today - target_date
        return delta.days

    except ValueError:
       return None
