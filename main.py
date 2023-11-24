# Определение структуры STUDENT
class STUDENT:
    def __init__(self, name, group, grades):
        self.name = name
        self.group = group
        self.grades = grades

# Ввод данных в массив структур типа STUDENT
students = []
for i in range(1):
    name = input("Введите фамилию и имя студента: ")
    group = input("Введите номер группы: ")
    grades = []
    for j in range(4):
        grade = float(input(f"Введите оценку за предмет {j+1}: "))
        grades.append(grade)
    student = STUDENT(name, group, grades)
    students.append(student)

# Поиск и вывод информации об обучающихся с средним баллом больше 75
found_students = False
for student in students:
    average_grade = sum(student.grades) / len(student.grades)
    if average_grade > 75:
        print(f"Фамилия и имя: {student.name}")
        print(f"Номер группы: {student.group}")
        found_students = True

# Если нет обучающихся с средним баллом больше 75, выводим сообщение
if not found_students:
    print("Нет обучающихся с средним баллом больше 75")

