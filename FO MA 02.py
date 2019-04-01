class DiplomaProgramme(object):
    """
        Takes in students, courses and teachers as input.
        Should be able to show an overview of the student's situation.
        Can add, remove and write students, courses and teachers.
    """
    diplomaProgramme_no = 0
    def __init__(self, diplomaName, courses = None, teachers = None, students = None):
        self.diplomaName = diplomaName
        if courses is None:
            self.courses = []
        else:
            self.courses = courses
        if teachers is None:
            self.teachers = []
        else:
            self.teachers = teachers
        if students is None:
            self.students = []
        else:
            self.students = students
    def __str__(self):
        return "Diploma programme: " + str(self.diplomaName)

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
            Course.course_no -= 1
    def print_courses(self):
        self.courses.sort()
        print '\n    The diploma programme ' + str(self.diplomaName) + ' is offering following courses:\n'
        for course in sorted(self.courses):
            print('--> ' + str(course.courseName))

    def add_teacher(self, teacher):
        if teacher not in self.teachers:
            self.teachers.append(teacher)
    def remove_teacher(self, teacher):
        if teacher in self.teacher:
            self.teacher.remove(teacher)
            Teacher.teacher_no -= 1
    def print_teachers(self):
        print "\n    The diploma programme " + str(self.diplomaName) + "'s faculty is made up of the following theachers:\n"
        for teacher in self.teachers:
            print('--> ' + teacher.fullName)

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            Student.student_no -= 1
    def print_students(self):
        print '\n    The diploma programme ' + str(self.diplomaName) + ' has enrolled the following students:\n'
        for student in self.students:
            print('--> ' + str(student.fullName))

    def overview(self):
        for student in self.students:
            student.graduated()
    def count_overview(self):
        graduated_counter = 0
        not_graduated_counter = 0
        for student in self.students:
            if student.graduated() == True:
                graduated_counter += 1
            elif student.graduated() == False:
                not_graduated_counter += 1
        print "\nGraduated students: " + str(graduated_counter) + "/" + str(Student.student_no)
        print "Students not graduating: " + str(not_graduated_counter) + "/" + str(Student.student_no) + '\n'
    def distinction_overview(self):
        distinction_counter = 0
        print('\n')
        for student in self.students:
            if student.distinction() == True:
                print('--> ' + str(student.fullName) + ' has obtained a distinction.')
                distinction_counter += 1
        if distinction_counter == 0:
            print('No students with distinction.')


class Course(object):
    course_no = 0
    """
    Input: name, teachers.
    Should be abe to do: add/remove/print teachers.
    """
    def __init__(self, courseName, teachers = None):
        self.courseName = courseName
        if teachers is None:
            self.teachers = []
        else:
            self.teachers = teachers
        Course.course_no += 1
    def __str__(self):
        return "Course: " + str(self.courseName)

    def set_courseName(self, name):
        self.courseName = name
    def get_courseName(self):
        return self.courseName

    def add_teacher(self, teacher):
        if teacher not in self.teachers:
            self.teachers.append(teacher)
    def remove_teacher(self, teacher):
        if teacher in self.teacher:
            self.teacher.remove(teacher)
    def print_teachers(self):
        print '\n    ' + self.get_courseName() + ' is taught by:\n'
        for teacher in self.teachers:
            print('--> ' + teacher.fullName)

class Person(object):
    """
        Should serve as a super-class for Teacher and Student.
    """
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
    def __str__(self):
        return "Person: " + str(self.firstName) + " " + str(self.lastName)
    def get_firstName(self):
        return self.firstName
    def get_lastName(self):
        return self.lastName
    def set_firstName(self, new_firstName):
        self.firstName = new_firstName
    def set_lastName(self, new_lastName):
        self.lastName = new_lastName
    @property
    def fullName(self):
        return '{} {}'.format(self.firstName, self.lastName)
    def set_fullName(self, name):
        firstName, lastName = name.split(' ')
        self.firstName = firstName
        self.lastName = lastName
    def get_fullName(self):
        return self.fullName
    def delete_fullName(self):
        self.fullName = None
        self.firstName = None
        self.lastName = None

class Teacher(Person):
    """
        Input: first name, last name, courses taught.
        Should be able to: add/remove/print courses.
    """
    teacher_no = 0
    def __init__(self, firstName, lastName, courses = None):
        Person.__init__(self, firstName, lastName)
        if courses is None:
            self.courses = []
        else:
            self.courses = [courses]
        Teacher.teacher_no += 1

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
    def print_courses(self):
        self.courses.sort()
        print '\n    ' + str(self.firstName) + ' teaches the following courses:\n'
        for course in sorted(self.courses):
            print('--> ' + str(course.courseName))


class Student(Person):
    """
        Should return name of student, programme, courses (dictionary keys), grades
    (values = number of assignments completed/ course), distinction (true or false).
        Should be able to add/substract/change courses and their values.
    """
    student_no = 0 # We might to count the number of students enrolled in our program.
    def __init__(self, firstName, lastName, courses = None, grades = None, passed_failed = None):
        Person.__init__(self, firstName, lastName)
        if courses is None:
            self.courses = []
        else:
            self.courses = courses
        if grades is None:
            self.grades = {}
        else:
            self.grades = {grades}
        Student.student_no += 1
        if passed_failed is None:
            self.passed_failed = {}
        else:
            self.passed_failed = {passed_failed}
    def __str__(self):
        return "Student: " + str(self.firstName) + " " + str(self.lastName)

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
    def print_courses(self):
        self.courses.sort()
        print '\n    ' + str(self.firstName) + ' is enrolled in the following courses:\n'
        for course in sorted(self.courses):
            print('--> ' + str(course.courseName))

    def set_grade(self, course, assignments_completed):
        if (assignments_completed >= 0) and (assignments_completed <= 5):
                self.grades[course] = assignments_completed
        else:
            print('Error: The number of mandatory assignments completed must be between 0 and 5.')
    def increase_grade(self, course):
        if course in self.grades:
            if self.grades[course] < 5:
                self.grades[course] += 1
            else:
                print('Error: The student ' + str(self.fullName) + ' has already completed all 5 mandatory assignments for the course ' + str(course) + '.')
    def decrease_grade(self, course):
        if course in self.grades:
            if self.grades[course] > 0:
                self.grades[course] -= 1
            else:
                print('Error: The student ' + str(self.fullName) + ' can not have a negative grade on his mandatory assignments for course ' + str(course) + '.')
    def print_grades(self):
        print '\n    ' + str(self.firstName) + ' has completed the following number of assignments for each course:\n'
        for grade in sorted(self.grades.keys()):
            print('--> ' + str(grade) + ': ' + str(self.grades[grade]))

    def set_passed_failed(self):
        for course in self.grades:
            if self.grades[course] < 3:
                self.passed_failed[course] = 'Failed'
            else:
                self.passed_failed[course] = 'Passed'
    def print_passed_failed(self):
        print '\n    ' + str(self.firstName) + ' has passed or failed the following courses:\n'
        for course in sorted(self.passed_failed.keys()):
            print('--> ' + str(course) + ': ' + str(self.passed_failed[course]))

    def graduated(self):
        graduated = True
        for grade in self.passed_failed.values():
            if grade == 'Failed':
                graduated = False
                break
        if graduated == True:
            return True
            #print '\n    ' + str(self.fullName) + ' has graduated the programme.'
        else:
            return False
            #print '\n    ' + str(self.fullName) + ' has not graduated the programme.'
    def distinction(self):
        distinction = False
        for grade in self.grades.values():
            if grade == 5:
                distinction = True
                break
        if (sum(self.grades.values()) >= 17) and distinction == True: # Perhaps we might want to extend this method. We can always have let's say 5 or more courses in a programme.
            #print '\n' + str(self.fullName) + ' has earned a distinction diploma.'
            return True
        else:
            return False
            #print '\n' + str(self.fullName) + ' has not earned a distinction diploma.'

# <<<< COURSES >>>>>
course_names = ["Data Mining, Machine Learning and Deep Learning", "Foundations of Data Science", "Text Analytics", "Visual Analytics"]
c1 = Course(course_names[0])
c2 = Course(course_names[1])
c3 = Course(course_names[2])
c4 = Course(course_names[3])
courses = [c1, c2, c3, c4]

# <<<<< TEACHERS >>>>>
t1 = Teacher('John', 'Doe', c1)
t2 = Teacher('Christian', 'Sondegaard', c2)
t3 = Teacher('Peter', 'Bush', c3)
t4 = Teacher('Maria','Castro') # Not initialized with any course.
t5 = Teacher('Marius', 'Negoita', c1)
teachers = [t1, t2, t3, t4, t5]
t4.add_course(c4) # Another way of assigning a course.

# <<<<< STUDENTS >>>>>
s1 = Student('Alin', 'Preda', courses)
s2 = Student('Aristotelis', 'Stomapoulos', courses)
s3 = Student('Maria', 'Tureschi') # Not initialized with courses.
s3.add_course(courses) # Another way to add a student's courses.
students = [s1, s2, s3]

# <<<<<< ASSIGNING >>>>>>>>
c1.add_teacher(t1)
c1.add_teacher(t2)
c2.add_teacher(t2)
c3.add_teacher(t3)
c4.add_teacher(t4)

s1.set_grade(c1.courseName, 4)
s1.set_grade(c2.courseName, 4)
s1.set_grade(c3.courseName, 2)
s1.set_grade(c4.courseName, 5)

s2.set_grade('Data Mining, Machine Learning and Deep Learning', 4)
s2.set_grade(c2.courseName, 3)
s2.set_grade(c3.courseName, 4)
s2.set_grade('Visual Analytics', 4)

s3.set_grade(c1.courseName, 4)
s3.set_grade(c2.courseName, 4)
s3.set_grade(c3.courseName, 4)
s3.set_grade(c4.courseName, 4)

# <<<<<< PRINT METHODS >>>>>>>
s1.print_courses()
s1.set_passed_failed()
s1.print_passed_failed()
s1.print_grades()
print('\nHas Alin graduated?')
print(s1.graduated())
print('\nHas Alin obtained a distinction?')
print(s1.distinction())

s2.print_courses()
s2.print_grades()
s2.set_passed_failed()
s2.print_passed_failed()
print('\nHas Aris graduated?')
print(s2.graduated())
print('\nHas Aris obtained a distinction?')
print(s2.distinction())


s3.increase_grade(c1.courseName)
s3.decrease_grade('Visual Analytics')
s3.print_grades()
s3.set_passed_failed()
s3.print_passed_failed()
print('\nHas Maria graduated?')
print(s3.graduated())



# <<<<< DIPLOMA PROGRAMME >>>>
dp = DiplomaProgramme("Data Science", courses, teachers, students)
dp.print_teachers()
dp.print_courses()
dp.print_students()
dp.overview()
dp.count_overview()
dp.distinction_overview()
s4 = Student('Tommy', 'Ashad')
dp.add_student(s4)
dp.print_students()
print(Student.student_no)
dp.remove_student(s4)
dp.print_students()
t5 = Teacher('Mel', 'Gibson', c4)
dp.add_teacher(t5)
dp.print_teachers()
# print(t2.courses)
# t2.print_courses()
c5 = Course('Web scrapping')
t2.print_courses()
dp.add_course(c5)
dp.print_courses()
dp.remove_course(c5)
dp.print_courses()
print(Course.course_no)
