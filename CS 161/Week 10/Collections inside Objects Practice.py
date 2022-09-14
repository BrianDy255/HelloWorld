#Replace all occurences of BLANK with appropriate terms in the code below to make it work!

class Student:
    """
    Class for a Student Object that can enrol for courses and withdrawm from courses
    """
    def __init__(self, onid):
        print("Initializing student object for ONID ", onid)
        self._courses_enrolled = {}
        self._onid = onid

    def enrol_for_course(self, course_number, course_name):
        print("Enrolling for course", course_name, course_number)
        self._courses_enrolled[course_number] = course_name

    def withdraw_from_course(self, course_number):
        print("Withdrawing from course", course_number)
        self._courses_enrolled.pop(course_number)

    def print_enrolled_courses(self):
        print("Courses this student has enrolled for")
        print(self._courses_enrolled)

s1 = Student("93313339X")
s1.enrol_for_course('CS161', "Introduction to Computer Science I")
s1.enrol_for_course('CS361', "Software Engineering I")
s1.print_enrolled_courses()
s1.withdraw_from_course("CS361")
s1.print_enrolled_courses()