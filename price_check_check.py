import datetime


def price_check_check():
    # between saturday 11:55am and 12:30pm UTC
    if (
        datetime.datetime.utcnow().weekday() == 5 and
        datetime.datetime.utcnow().hour == 11 and
        datetime.datetime.utcnow().minute >= 55
    ):
        return "Price check check passed"
    return "Price check check test passed"
