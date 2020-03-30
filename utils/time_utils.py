from datetime import datetime, timedelta, timezone


def is_within_minutes(iso_datetime, minutes=30):
    return datetime.fromisoformat(iso_datetime) + timedelta(minutes=minutes) >= datetime.now(timezone.utc)
