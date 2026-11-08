from name import Name
from date import Date

class Student:
    def __init__(self, code: str = "", name: Name = None, birthDate: Date = None, career: str = "", startDate: Date = None, grade: float = 0.0):
        self._code = code
        self._name = name
        self._birthDate = birthDate
        self._career = career
        self._startDate = startDate
        self._grade = grade

    def __str__(self):
        return f"{self._code} | {self._name} | {self._birthDate} | {self._career} | {self._startDate} | {self._grade}"

    @property
    def code(self) -> str:
        return self._code

    @code.setter
    def code(self, value: str):
        self._code = value

    @property
    def name(self) -> Name:
        return self._name

    @code.setter
    def name(self, value: Name):
        self._name = value

    @property
    def birth_date(self) -> Date:
        return self._birthDate

    @birth_date.setter
    def birth_date(self, value: Date):
        self._birthDate = value

    @property
    def career(self) -> str:
        return self._career

    @career.setter
    def career(self, value: str):
        self._career = value

    @property
    def start_date(self) -> Date:
        return self._startDate

    @start_date.setter
    def start_date(self, value: Date):
        self._startDate = value

    @property
    def grade(self) -> str:
        return self._grade

    @grade.setter
    def grade(self, value: float):
        self._grade = value
