from datetime import datetime, timedelta, timezone


def is_within_hours(iso_datetime, hours=1):
    return round_down_to_half_hour(datetime.now(timezone.utc)) + timedelta(minutes=30) > datetime.fromisoformat(iso_datetime) + timedelta(hours=hours) >= round_down_to_half_hour(datetime.now(timezone.utc))


def round_down_to_half_hour(date_time: datetime):
    return date_time.replace(minute=0, second=0, microsecond=0) if date_time.minute in range(0, 30) else date_time.replace(minute=30, second=0, microsecond=0)
