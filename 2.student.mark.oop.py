
class Student:
    def __init__(self, studentId, studentName, studentDob = None):
        self.__studentId = studentId
        self.__studentName = studentName
        self.__studentDob = studentDob
        self.__studentMark = {}
    
    def getStudentId(self):
        return self.__studentId
    
    def getStudentName(self):
        return self.__studentName
    
    def getStudentDob(self):
        return self.__studentDob
    
    def setStudentMark(self, Course):
        mark = float(input("Enter mark for {}:".format(Course.getCourseName())))
        self.__studentMark['{}'.format(Course.getCourseName())] = mark
    
    def getStudentMark(self, courseName):
        return self.__studentMark['{}'.format(courseName)]
        
        
class Course:
    def __init__(self, courseId, courseName):
        self.__courseName = courseName
        self.__courseId = courseId
        
    def getCourseName(self):
        return self.__courseName

    def getCourseId(self):
        return self.__courseId
        
class Class:
    def __init__(self):
        self.__studentList = []
        self.__courseList = []
    # Add student to class    
    def initStudent(self, Student):
        self.__studentList.append(Student)
    # Add course to class
    def initCourse(self, Course):
        self.__courseList.append(Course)
    # Set mark for specific course    
    def setMark(self, Course):
        for student in self.__studentList:
            print("Student name: {}".format(student.getStudentName()))
            student.setStudentMark(Course)
            
    # Getter for student and course list
    def getStudentList(self):
        return self.__studentList
    def getCourseList(self):
        return self.__courseList

def main():
    # Create new Class object
    newClass = Class()
    
    print("STUDENT MARK MANAGEMENT")
    while True:
        # Option table
        print()
        print("Option:")
        print("--- 1 --- Add student to class.")
        print("--- 2 --- Add course.")
        print("--- 3 --- Input mark.")
        print("--- 4 --- Courses list.")
        print("--- 5 --- Student list.")
        print("--- 6 --- Student's mark for course.")
        print("--- 0 --- Exit!")
        option = int(input("Choose option: "))
        print("---------")
        print("Option {} choosing...".format(option))
        
        if option == 1:
            print("Add student to class:")
            numberOfStudents = int(input("Enter the number of students: "))
            for i in range(numberOfStudents):
                print("----------")
                while True:
                    duplicate = False
                    studentId = input("Enter student {} ID: ".format(i+1))
                    for student in newClass.getStudentList():
                        existedStudentId = student.getStudentId()
                        if studentId == existedStudentId:
                            duplicate = True
                            print("Duplicate student ID. Please re-enter!!!")
                    if duplicate == False: 
                        break
                
                studentName = input("Enter student name: ")
                studentDob = input("Enter student date of birth: ")
                newStudent = Student(studentId = studentId, studentName = studentName, studentDob = studentDob)
                print("----------")
                newClass.initStudent(newStudent)
            print("Add students DONE!!!")
        
        elif option == 2:
            print("Add subject:")
            numberOfCourses = int(input("Enter the number of courses: "))
            for i in range(numberOfCourses):
                print("----------")
                while True:
                    duplicate = False
                    courseId = input("Enter course {} ID: ".format(i+1))
                    for course in newClass.getCourseList():
                        if courseId == course.getCourseId():
                            duplicate = True
                            print("Duplicate course ID. Please re-enter!!!")
                    if duplicate == False: 
                        break
                
                courseName = input("Enter course name: ")
                newCourse = Course(courseId=courseId, courseName=courseName)
                print("----------")
                newClass.initCourse(newCourse)
            print("Add courses DONE!!!")

        elif option == 3:
            print("Input mark: ")
            while True:    
                course = input("Enter the course: ")
                courseFound = False
                for existCourse in newClass.getCourseList():
                    if course == existCourse.getCourseName():
                        courseFound = True
                        currentCourse = existCourse
                        break
                if courseFound == True:
                    print("Course found!")
                    break
                else:
                    print("No course found! Please re-try!")
            newClass.setMark(currentCourse)
            print("Add courses DONE!!!")        

        elif option == 4:
            print ("Course list: ")
            for course in newClass.getCourseList():
                print("{} - {}".format(course.getCourseId(), course.getCourseName()))
            print("Display course list DONE!!!") 
            
        elif option == 5:
            print("Student list: ")
            for student in newClass.getStudentList():
                print("ID: {} - Name: {} - DOB: {}".format(student.getStudentId(), student.getStudentName(), student.getStudentDob()))
            print("Display student list DONE!!!") 

        elif option == 6:
            print("Student's marks for course:")
            courseFound = False
            while True:
                course = input("Enter course: ")
                for c in newClass.getCourseList():
                    if c.getCourseName() == course:
                        courseFound = True
                        for student in newClass.getStudentList():
                            print("ID: {} - Student name: {} - Mark: {}".format(student.getStudentId(), student.getStudentName(), student.getStudentMark(course)))
                        break
                if courseFound == True:
                    break
                else:
                    print("No course found! Please re-try!")
            print("Display students marks for {} DONE!!!".format(course))     
        
        elif option == 0:
            print ("Exit!!!!")
            break
        
        else:
            print("No option available! Please re-enter!!!")
    
    
if __name__ == "__main__":
    main()
    
    
        