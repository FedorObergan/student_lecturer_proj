class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _mean_grade(self):
        full_sum = 0
        full_len = 0
        for value in self.grades.values():
            full_sum += sum(value)
            full_len += len(value)
        if full_len == 0:
            return 0
        else:
            return full_sum/full_len

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self._mean_grade()}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")

    def __eq__(self, other):
        return self._mean_grade() == other._mean_grade()

    def __lt__(self, other):
        return self._mean_grade() < other._mean_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _mean_grade(self):
        full_sum = 0
        full_len = 0
        for value in self.grades.values():
            full_sum += sum(value)
            full_len += len(value)
        if full_len == 0:
            return 0
        else:
            return full_sum/full_len

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self._mean_grade()}")

    def __eq__(self, other):
        return self._mean_grade() == other._mean_grade()

    def __lt__(self, other):
        return self._mean_grade() < other._mean_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}")


student_1 = Student('Иван', 'Сидоров', 'м')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование']
student_2 = Student('Евгения', 'Маркова', 'ж')
student_2.courses_in_progress += ['Python', 'Git', 'SQL']
student_2.finished_courses += ['Введение в программирование', 'Java']

lecturer_1 = Lecturer('Владимир', 'Крамской')
lecturer_1.courses_attached += ['Python']
lecturer_2 = Lecturer('Игорь', 'Понкратов')
lecturer_2.courses_attached += ['Git', 'SQL']

reviewer_1 = Reviewer('Виктор', 'Спичкин')
reviewer_1.courses_attached += ['Python']
reviewer_2 = Reviewer('Марк', 'Абрамов')
reviewer_2.courses_attached += ['Git', 'SQL']

student_1.rate_lecturer(lecturer_1, 'Python', 8)
student_1.rate_lecturer(lecturer_2, 'Git', 9)
student_1.rate_lecturer(lecturer_2, 'SQL', 7)
student_2.rate_lecturer(lecturer_1, 'Python', 9)
student_2.rate_lecturer(lecturer_2, 'Git', 7)
student_2.rate_lecturer(lecturer_2, 'SQL', 7)

reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_2, 'Python', 6)
reviewer_2.rate_hw(student_1, 'Git', 5)
reviewer_2.rate_hw(student_2, 'Git', 8)
reviewer_2.rate_hw(student_2, 'SQL', 7)

print(student_2)
print()
print(reviewer_1)
print()
print(lecturer_2)
print()
print(student_1 < student_2)
print(lecturer_1 > lecturer_2)
print(lecturer_1 == lecturer_2)
print()

def mean_grade_hw_for_course(students, course_name):
    full_sum = 0
    full_len = 0
    for student in students:
        if course_name in student.courses_in_progress:
            full_sum += sum(student.grades[course_name])
            full_len += len(student.grades[course_name])
    if full_len == 0:
        return 0
    else:
        return full_sum/full_len

def mean_grade_lect_for_course(lecturers, course_name):
    full_sum = 0
    full_len = 0
    for lecturer in lecturers:
        if course_name in lecturer.courses_attached:
            full_sum += sum(lecturer.grades[course_name])
            full_len += len(lecturer.grades[course_name])
    if full_len == 0:
        return 0
    else:
        return full_sum/full_len


print(f"Средняя оценка по всем студентам по курсу Python: "
      f"{mean_grade_hw_for_course([student_1,student_2], 'Python')}")
print(f"Средняя оценка по всем студентам по курсу Git: "
      f"{mean_grade_hw_for_course([student_1,student_2], 'Git')}")
print(f"Средняя оценка по всем студентам по курсу SQL: "
      f"{mean_grade_hw_for_course([student_1,student_2], 'SQL')}")
print()
print(f"Средняя оценка по всем лекторам по курсу Python: "
      f"{mean_grade_lect_for_course([lecturer_1,lecturer_2], 'Python')}")
print(f"Средняя оценка по всем лекторам по курсу Git: "
      f"{mean_grade_lect_for_course([lecturer_1,lecturer_2], 'Git')}")
print(f"Средняя оценка по всем лекторам по курсу SQL: "
      f"{mean_grade_lect_for_course([lecturer_1,lecturer_2], 'SQL')}")