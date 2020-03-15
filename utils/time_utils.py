from datetime import datetime, timedelta, timezone


def is_within_hours(iso_datetime, hours=4):
    return datetime.fromisoformat(iso_datetime) + timedelta(hours=hours) >= datetime.now(timezone.utc)
