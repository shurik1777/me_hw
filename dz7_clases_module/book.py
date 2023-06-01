class Student:
    def __init__(self, _name):
        self.name = _name
        self.grades = {}

    def add_grade(self, _subject, grade):
        if _subject not in self.grades:
            self.grades[_subject] = []
        self.grades[_subject].append(grade)

    def get_average_grade(self, subject_=None):
        if subject_ is None:
            grades_list = []
            for subject_grades in self.grades.values():
                grades_list.extend(subject_grades)
            return sum(grades_list) / len(grades_list)
        else:
            return sum(self.grades[subject_]) / len(self.grades[subject_])


class Journal:
    def __init__(self, subjects):
        self.subjects = subjects
        self.students = {}

    def add_student(self, _name):
        self.students[_name] = Student(_name)

    def add_grade(self, _name, _subject, grade):
        self.students[_name].add_grade(_subject, grade)

    def get_last_name(self, full_name):
        return full_name.split()[-1]

    def print_student_grades(self, _name):
        student = self.students[_name]
        print(f"Студент: {student.name}")
        for subj, grades in student.grades.items():
            average_grade = sum(grades) / len(grades)
            print(f"{subj}: {grades} (средний балл: {average_grade})")
        average_grade = student.get_average_grade()
        print(f"Средний балл за все предметы: {average_grade}")

    def print_subject_grades(self, subj):
        grades_list = []
        for student in self.students.values():
            if subj in student.grades:
                grades_list.extend(student.grades[subj])
        average_grade = sum(grades_list) / len(grades_list)
        print(f"Средний балл за предмет {subj}: {average_grade}")


journal = Journal(["математика", "физика", "химия", "английский язык"])

journal.add_student("Иванов Иван Иванович")
journal.add_student("Петров Александр Иванович")
journal.add_student("Сидорова Екатерина Сергеевна")

journal.add_grade("Иванов Иван Иванович", "математика", 5)
journal.add_grade("Иванов Иван Иванович", "математика", 4)
journal.add_grade("Иванов Иван Иванович", "физика", 3)
journal.add_grade("Иванов Иван Иванович", "физика", 4)
journal.add_grade("Иванов Иван Иванович", "химия", 4)
journal.add_grade("Петров Александр Иванович", "математика", 4)
journal.add_grade("Петров Александр Иванович", "физика", 5)
journal.add_grade("Петров Александр Иванович", "химия", 5)
journal.add_grade("Петров Александр Иванович", "английский язык", 4)
journal.add_grade("Сидорова Екатерина Сергеевна", "английский язык", 5)

name = "Петров Александр Иванович"
journal.print_student_grades(name)

subject = "математика"
journal.print_subject_grades(subject)

"""
Комментарии:

1. Создан класс Student (студент), у которого есть имя и список оценок по предметам.
2. Класс Journal (журнал) представляет собой коллекцию студентов и предметов. У него есть методы для добавления студента, добавления оценки студенту по предмету, вывода ведомости студента и вывода средней оценки по предмету.
3. Для получения средней оценки по всем предметам используется метод get_average_grade класса Student, который принимает опциональный аргумент subject (предмет), чтобы получить среднюю оценку только по определенному предмету.
4. Для получения фамилии студента из полного имени используется метод get_last_name класса Journal.
5. Пример заполнения журнала и вывода ведомости и средней оценки по предмету."""
