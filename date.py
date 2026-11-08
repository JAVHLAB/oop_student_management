

class Date:
    def __init__(self, year: int = 1970, month: int = 1, day: int = 1):
        self._year = year
        self._month = month
        self._day = day

    def __str__(self) -> str:
        return f"{self._day:02d}/{self._month:02d}/{self._year:04d}"
    
    def _is_leap_year(self) -> bool:
        return (self._year % 4 == 0 and self._year % 100 != 0) or (
            self._year % 400 == 0
        )

    def _days_in_month(self) -> int:
        if self._month in (1,3,5,7,8,10,12):
            return 31;
        if self._month in (4,6,9,11):
            return 30;
        return 29 if self._is_leap_year() else 28

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, value: int):
        if not(1900 <= value <= 2100):
            raise ValueError(f"Año inválido: {value}. Debe estar entre 1900 y 2100")
        self._year = value

    @property
    def month(self) -> int:
        return self._month

    @month.setter
    def month(self, value: int):
        if not(1 <= value <= 12):
            raise ValueError(f"Mes inválido: {value}. Debe estar entre 1 y 12")
        self._month = value

    @property
    def day(self) -> int:
        return self._day

    @day.setter
    def day(self, value: int):
        max_days = self._days_in_month()
        if not (1 <= value <= max_days):
            raise ValueError(f"Día inválido: {value}. El mes {self._month} del año {self._year} solo tiene {max_days} días.")
        self._day = value

    @property
    def to_int(self) -> int:
        return self._year*10000 + self._month*100 + self._day



"""
d1 = Date(1996, 5, 21)

d1.day = 20

print(d1.to_int)
print(d1.day)
print(d1)
"""
