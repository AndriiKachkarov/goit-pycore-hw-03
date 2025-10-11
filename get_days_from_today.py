from datetime import datetime


def get_days_from_today(date: str) -> int:
    """
    Calculates the number of days from today to the given date.
    """
    try:
        target_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()

        delta = today - target_date
        return delta.days

    except ValueError:
        raise ValueError("Wrong date format, should be YYYY-MM-DD")
