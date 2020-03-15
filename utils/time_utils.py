from datetime import timedelta, timezone


def is_within_hours(datetime, hours=4):
    return datetime.fromisoformat(datetime) + timedelta(hours=hours) >= datetime.now(timezone.utc)
