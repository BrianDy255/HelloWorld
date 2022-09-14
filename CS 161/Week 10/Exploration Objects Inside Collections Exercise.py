#Replace all occurences of BLANK with appropriate terms in the code below to make it work!
class Course:
    def __init__(self, number, name):
        self._name = name
        self._number = number

    def get_name(self):
        return self._name

class Instructor:
    """
    Class for a Instructor Object that can teach courses
    """
    def __init__(self, name):
        print("Initializing Instructor object for name ", name)
        self._name = name
        #_courses_enrolled will be the data member which is a collection of objects
        self._courses_enrolled = []

    def teach_course(self, class_name):
        print("Teaching course", class_name.get_name())
        #add course to the _courses_enrolled collection
        self._courses_enrolled.append(class_name)

    def print_courses(self):
        print("Courses this Instructor is going to teach: ")
        for course in self._courses_enrolled:
            print(course.get_name())

#create objects
instructor_1 = Instructor("ABC")
cs161_course = Course("CS161", "Introduction to Computer Science I")
cs162_course = Course("CS162", "Introduction to Computer Science II")

#now call methods
instructor_1.teach_course(cs161_course)
instructor_1.teach_course(cs162_course)
instructor_1.print_courses()

#Debug and fix this piece of code to make it work

class Course:
    def __init__(self, number, name):
        self._name = name
        self._number = number

    def get_name(self):
        return self._name

cs161_course = Course("CS161", "Introduction to Computer Science I")
cs162_course = Course("CS162", "Introduction to Computer Science II")

list_of_courses = {cs161_course, cs162_course}

dictionary_of_courses = {"CS161":cs161_course, "CS162": cs162_course}
print(dictionary_of_courses['CS161'].get_name())
print(dictionary_of_courses['CS162'].get_name())