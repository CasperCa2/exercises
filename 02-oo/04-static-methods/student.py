class Duration():

    def __init__(self, duration_in_seconds):
        self.duration = duration_in_seconds

    @property
    def seconds(self):
        return self.duration

    @staticmethod
    def from_seconds(amount):
        return Duration(amount)

    @property
    def minutes(self):
        return self.duration/60

    @staticmethod
    def from_minutes(amount):
        return Duration(amount*60)

    @property
    def hours(self):
        return self.duration/3600

    @staticmethod
    def from_hours(amount):
        return Duration(amount*3600)
