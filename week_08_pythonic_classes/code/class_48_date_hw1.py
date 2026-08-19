# 1. Date class banao with from_string("2026-06-28") classmethod (year, month, day mein todo).

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    @classmethod
    def from_string(cls, text):
        y,m,d = text.split("-")
        return cls(int(y), int(m), int(d))

date = Date.from_string("2026-06-28")
print(date.year, date.month, date.day)  