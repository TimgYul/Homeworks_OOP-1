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
        return summ / count

    def __str__(self):
        average = Lecturer.average(self)
        res = f'\nИмя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {average}'
        return res
    

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
        if isinstance(lecture, Lecturer) and course in lecture.courses_attached: # and course in lecture.courses_in_progress:
            if course in lecture.grades:
                lecture.grades[course] += [grade]
            else:
                lecture.grades[course] = [grade]
        else:
            return 'Ошибка'     
    
    #def average(self):

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
    

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

cool_lecture = Lecturer('Any', 'Many') 
cool_lecture.courses_attached += ['Python']
best_student.rate_lecture(cool_lecture, 'Python', 10) 

print(best_student.grades)
print(cool_lecture.grades)
print(cool_reviewer)
print(cool_lecture)