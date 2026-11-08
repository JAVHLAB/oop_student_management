from student import Student
from date import Date
from name import Name


grupo = [Student() for i in range(2)]
myDate = Date()
myName = Name()

for alumno in grupo:
    print(f"\n--- Ingresando datos del estudiante ---")

    try:
        alumno.code = input("\nCodigo del alumno: ")

        alumno.name = Name(
            input("\nNombre del alumno: "),
            input("\nApellido del alumno: ")
        )

        alumno.birth_date = Date(
            int(input("\nAño de nacimiento: ")),
            int(input("\nMes de nacimiento: ")),
            int(input("\nDia de nacimiento: "))
        )

        alumno.career = input("\nCarrera: ")

        alumno.start_date = Date(
            int(input("\nAño de ingreso: ")),
            int(input("\nMes de ingreso: ")),
            int(input("\nDia de ingreso: "))
        )
        
        alumno.grade = input("\nCalificación del alumno: ")

    except ValueError as e:
        print(f"❌ Error al guardar: {e}")        

for alumno in grupo:
    print(alumno)

""" 
myStudent = Student()

myStudent.code = "211494331"

myName.first_name = "Javier"
myName.last_name = "Mariscal"

myStudent.name = myName

myDate.year = 1996
myDate.month = 5
myDate.day = 21

myStudent.birth_date = myDate

myStudent.career = "INNI"

myDate.year = 2022
myDate.month = 6
myDate.day = 15

myStudent.start_date = myDate

myStudent.grade = 96.5

print(myStudent)
"""