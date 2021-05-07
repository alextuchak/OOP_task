class Student:
    student_list = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.student_list.append(self)
    def rate_lt (self, lectors, course, grade):
        if isinstance(lectors, Lectors) and course in self.courses_in_progress and course in lectors.courses_attached:
            if grade not in range(0, 11):
                print('Оценка выставляется по 10-ти бальной шкале!')
                return
            elif course in lectors.grades:
                lectors.grades[course] += [grade]
            else:
                lectors.grades[course] = [grade]
        else:
            return 'Ошибка'
    def avr_hw_grade(student_list, course):
        grades_sum = 0
        grades_quantity = 0
        for el in student_list:
            for k in el.grades.keys():
                if k == course:
                    grades_quantity += len(el.grades.get(k))
                    for v in el.grades.get(k):
                        grades_sum += v
        print(float(grades_sum / grades_quantity))
    def avr_grade (self):
        grades_sum = 0
        grades_quantity = 0
        for k in self.grades.keys():
            grades_quantity += len(self.grades.get(k))
            for v in self.grades.get(k):
                grades_sum += v
        return float(grades_sum / grades_quantity)
    def __lt__(self, other):
        if not isinstance(other, Student):
            print(f'{other} не является студентом')
            return
        return self.avr_grade() < other.avr_grade()
    def __str__(self):
        return (f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.avr_grade()} \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \nЗавершенные курсы: {", ".join(self.finished_courses)} ' )

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
class Lectors (Mentor):
    lectors_list = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        Lectors.lectors_list.append(self)
    def avr_grade (self):
        grades_sum = 0
        grades_quantity = 0
        for k in self.grades.keys():
            grades_quantity += len(self.grades.get(k))
            for v in self.grades.get(k):
                grades_sum += v
        return float(grades_sum / grades_quantity)
    def avr_lct_grade(lectors_list, course):
        grades_sum = 0
        grades_quantity = 0
        for el in lectors_list:
            for k in el.grades.keys():
                if k == course:
                    grades_quantity += len(el.grades.get(k))
                    for v in el.grades.get(k):
                        grades_sum += v
        print(float(grades_sum / grades_quantity))
    def __lt__(self, other):
        if not isinstance(other, Lectors):
            print(f'{other} не является лектором')
            return
        return self.avr_grade() < other.avr_grade()
    def __str__(self):
        return (f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.avr_grade()}')
class Reviewer (Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return (f'Имя: {self.name} \nФамилия: {self.surname}')


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['С+']
best_student.finished_courses += ['С#']

lazy_student = Student('Shrek', 'Swampson', 'male')
lazy_student.courses_in_progress += ['Python']
lazy_student.courses_in_progress += ['Git']
lazy_student.finished_courses += ['С+']
lazy_student.finished_courses += ['С#']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
reg_mentor = Mentor('Buddy', 'Some')
reg_mentor.courses_attached += ['Python']

cool_reviewer = Reviewer('Steve', 'jobs')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(lazy_student, 'Python', 8)
cool_reviewer.rate_hw(lazy_student, 'Git', 9)
cool_reviewer.rate_hw(best_student, 'Git', 8)

reg_reviewer = Reviewer('Vasya', 'Pupkin')
reg_reviewer.courses_attached += ['Python']
reg_reviewer.courses_attached += ['Git']
reg_reviewer.rate_hw(best_student, 'Python', 7)
reg_reviewer.rate_hw(lazy_student, 'Python', 6)
reg_reviewer.rate_hw(lazy_student, 'Git', 8)
reg_reviewer.rate_hw(best_student, 'Git', 9)

cool_lector = Lectors ('Sergey', 'Brin')
cool_lector.courses_attached += ['Python']
cool_lector.courses_attached += ['Git']
best_student.rate_lt(cool_lector, 'Python', 10)
best_student.rate_lt(cool_lector, 'Git', 9)
lazy_student.rate_lt(cool_lector, 'Python', 9)
lazy_student.rate_lt(cool_lector, 'Git', 8)

reg_lector = Lectors('Ivan', 'Kuznetcov')
reg_lector.courses_attached += ['Python']
reg_lector.courses_attached += ['Git']
best_student.rate_lt(reg_lector, 'Python', 10)
best_student.rate_lt(reg_lector, 'Git', 9)
lazy_student.rate_lt(reg_lector, 'Python', 8)
lazy_student.rate_lt(reg_lector, 'Git', 8)

print(cool_reviewer)
print(reg_reviewer)
print(cool_lector)
print(reg_lector)
print(best_student)
print(lazy_student)
print(best_student > lazy_student)
print(cool_lector < reg_lector)

Student.avr_hw_grade(Student.student_list, 'Python')
Student.avr_hw_grade(Student.student_list, 'Git')

Lectors.avr_lct_grade(Lectors.lectors_list, 'Python')
Lectors.avr_lct_grade(Lectors.lectors_list, 'Git')