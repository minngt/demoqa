from datetime import datetime, timedelta

def convert_to_utc_string(date_time: str) -> str:
    return datetime.strptime(date_time, "%Y-%m-%dT%H:%M:%S").strftime('%a, %d %b %Y %H:%M:%S GMT')

def format_date(date):
    return date.strftime('%d/%m/%Y')

def tomorrow() -> str:
    return format_date(datetime.now() + timedelta(days=1))

def yesterday() -> str:
    return format_date(datetime.now() - timedelta(days=1))
