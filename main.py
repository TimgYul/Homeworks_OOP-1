from re import L
from statistics import mean

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
 
class Lecturer(Mentor):
    def __init__(self, name,surname):
        super().__init__(name, surname)
        self.grades = {}    
    
    def average(self):
        count = 0
        summ = 0
        for list in self.grades.values():
            count += len(list)
            summ += sum(list)
        if count != 0:
            return summ / count
        else:
            return 0

    def __str__(self):
        average = Lecturer.average(self)
        res = f'\nИмя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {average}'
        return res
    
    def __gt__(self, other):
        if not isinstance(other, Lecturer):# and not isinstance(self,Lecturer):
            print('Not a Character!')
            return
        return self.average() > other.average()

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_course.append(course_name)   
 
    def rate_lecture(self, lecture, course, grade):
        if isinstance(lecture, Lecturer) and course in lecture.courses_attached and course in self.courses_in_progress:
            if course in lecture.grades:
                lecture.grades[course] += [grade]
            else:
                lecture.grades[course] = [grade]
        else:
            return 'Ошибка'     
    
    def average_student(self):
        count = 0
        summ = 0
        for list in self.grades.values():
            count += len(list)
            summ += sum(list)
        
        if count != 0:
            return summ / count
        else:
            return 0

    

    def __str__(self):
        average = Student.average_student(self)
        res = f'\nИмя: {self.name} \nФамилия: {self.surname} \nСредняя оценки за домашние задания: {average}\nКурсы в процессе изучения:{self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
        return res
    
    def __gt__(self, other):
        if not isinstance(other, Student):# and not isinstance(self,Lecturer):
            print('Not a Character!')
            return
        return self.average_student() > other.average_student()

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
        res = f'\nИмя: {self.name} \nФамилия: {self.surname}'
        return res
    
student1 = Student('Ruoy', 'Eman', 'your_gender')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['C##']
student1.finished_courses += ['Java']

student2 = Student('Bill', 'Geits', 'your_gender')
student2.courses_in_progress += ['Python']
student2.courses_in_progress += ['Abap']
student2.finished_courses += ['SQL']

reviewer1 = Reviewer('Some', 'Buddy')
reviewer1.courses_attached += ['Python']
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 8)

reviewer1.rate_hw(student2, 'Python', 8)
reviewer1.rate_hw(student2, 'Abap', 10)

reviewer2 = Reviewer('Crtistian', 'Rouse')
reviewer2.courses_attached += ['Abap']
reviewer2.courses_attached += ['Python']

reviewer2.rate_hw(student1, 'Python', 5)
reviewer2.rate_hw(student1, 'Python', 6)
reviewer2.rate_hw(student1, 'Python', 8)

reviewer2.rate_hw(student2, 'Python', 10)
reviewer2.rate_hw(student2, 'Abap', 5)

lecture1 = Lecturer('Any', 'Many') 
lecture1.courses_attached += ['Python']
student1.rate_lecture(lecture1, 'Python', 10) 

lecture2 = Lecturer('Michel', 'Brown')
lecture2.courses_attached += ['Abap']
student2.rate_lecture(lecture2, 'Abap', 9.5)

print(student1.grades)
print(lecture1.grades)
print('\nREVIEWER')
print('-----------')
print(reviewer1)
print(reviewer2)
print('\nLECTURERS')
print('-----------')
print(lecture1)
print(lecture2)
print('\nSTUDENTS')
print('-----------')
print(student1)
print(student2)
print('-----------')
print(student2 > student1)
print(lecture1 < lecture2)

def average_all_grades(list, course):
    count = 0
    summ = 0
    grades = []
    if all([isinstance(item, Student) for item in list]):
        for student in list:
            if course in student.grades:
               count += len(student.grades[course])
               summ += sum(student.grades[course])

        if count != 0:
            return summ / count
        else:
            return 'Нет данных!'

    
    elif all([isinstance(item, Lecturer) for item in list]):
        for lecturer in list:
            if course in lecturer.grades:
              count += len(lecturer.grades[course])
              summ += sum(lecturer.grades[course])  

        if count != 0:
            return summ / count
        else:
            return 'Нет данных!'
    else:
        return 'Проверьте входные данные!'

print('\nСредняя оценка по курсу Python среди студентов:')
print(average_all_grades([student1,student2],'Python'))
print('\nСредняя оценка по курсу Abap среди лекторов:')
print(average_all_grades([lecture1,lecture2],'Abap'))
