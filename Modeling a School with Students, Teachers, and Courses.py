class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

    def display_info(self):
        course_list = ', '.join([course.name for course in self.courses])
        return f"{super().display_info()}, Student ID: {self.student_id}, Courses: {course_list}"

class Teacher(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.courses = []

    def assign_course(self, course):
        self.courses.append(course)

    def display_info(self):
        course_list = ', '.join([course.name for course in self.courses])
        return f"{super().display_info()}, Employee ID: {self.employee_id}, Courses: {course_list}"

class Course:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        student.enroll(self)

    def display_info(self):
        student_list = ', '.join([student.name for student in self.students])
        return f"Course: {self.name}, Code: {self.code}, Students: {student_list}"

# Example usage
course_math = Course("Mathematics", "MATH101")
course_english = Course("English", "ENG101")

student_1 = Student("Alice", 20, "S1001")
student_2 = Student("Bob", 22, "S1002")

teacher_1 = Teacher("Mr. Smith", 40, "T2001")

course_math.add_student(student_1)
course_math.add_student(student_2)

course_english.add_student(student_1)

teacher_1.assign_course(course_math)
teacher_1.assign_course(course_english)

print(student_1.display_info())
print(student_2.display_info())
print(teacher_1.display_info())
print(course_math.display_info())
print(course_english.display_info())
