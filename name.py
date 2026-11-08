import re

class Name:
    def __init__(self, firstName: str = " ", lastName: str = " "):
        self._firstName = firstName
        self._lastName = lastName

    def __str__(self) -> str:
        return f"{self._lastName} {self._firstName}"

    def _validate_name(self, name: str, field_name: str = "Nombre") -> str:
        if not isinstance(name, str):
            raise TypeError(f"El {field_name} debe ser texto, pero se recibió: {type(name).__name__}.")

        clean_name = name.strip()

        if not (2 <= len(clean_name) <= 50):
            raise ValueError(
                f"El {field_name} debe tener entre 2 y 50 caracteres "
                f"(longitud actual: {len(clean_name)})."
            )

        pattern = r"^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s\-']+$"
        if not re.match(pattern, clean_name):
            raise ValueError(
                f"El {field_name} '{clean_name}' contiene caracteres inválidos. "
                "Solo se permiten letras, espacios, guiones y apóstrofes."
            )

        return clean_name

    @property
    def first_name(self) -> str:
        return self._firstName

    @first_name.setter
    def first_name(self, value: str):
        self._firstName = self._validate_name(value, field_name="Nombre")

    @property
    def last_name(self) -> str:
        return self._lastName

    @last_name.setter
    def last_name(self, value: str):
        self._lastName = self._validate_name(value, field_name="Apellido")

"""
n1 = Name("Juan", "Lopez")

n1.first_name = "dr"
print(n1.last_name)
print(n1)
"""
