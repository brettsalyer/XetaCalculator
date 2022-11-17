from datetime import datetime, timedelta

class Xon:
    date_created = None
    date_expired = None
    expired = False
    xeta_rate = 0.1
    id = None

    date_format = "%Y-%m-%d"

    def __init__(self, id, date_created=datetime.today()) -> None:
        self.id = id
        self.date_created = date_created
        self.date_expired = date_created + timedelta(days=365)
    
    """
    Checks if a XON is expired today.

    :param today: todays date.
    :returns: True if the XON is expired, False otherwise.
    """
    def is_expired(self, today):
        days_left = self.date_expired - today

        if days_left.days < 1:
            self.expired = True
            return True
        
        return False

    """
    Simply stringifys the XON
    """
    def to_string(self):
        return f"XON: {self.id}"

    """
    Sets the current $X3TA rate.
    """
    def set_xeta_rate(self, rate):
        self.xeta_rate = rate