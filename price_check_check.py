import datetime


def price_check_check():
    # between saturday 11:00 and 14:00 UTC
    if (
        datetime.datetime.utcnow().weekday() == 5 and
        datetime.datetime.utcnow().hour >= 11 and
        datetime.datetime.utcnow().hour <= 14
    ):
        return "Price check check passed"
    return "Price check check has run the every time response"
