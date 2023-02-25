student_information = []
course_information = []
print("STUDENT MARK MANAGEMENT")
while True:
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
        number_of_students = int(input("Enter the number of students: "))
        for i in range(number_of_students):
            print("----------")
            while True:
                duplicate = False
                student_id = input("Enter student {} ID: ".format(i+1))
                for student in student_information:
                    if student_id == student["ID"]:
                        duplicate = True
                        print("Duplicate student ID. Please re-enter!!!")
                if duplicate == False: 
                    break
            
            student_name = input("Enter student name: ")
            student_dob = input("Enter student date of birth: ")
            new_student = dict(ID = student_id, Name = student_name, DOB = student_dob, Mark = [])
            print("----------")
            student_information.append(new_student)
        print("Add students DONE!!!")
    
    elif option == 2:
        print("Add subject:")
        number_of_courses = int(input("Enter the number of courses: "))
        for i in range(number_of_courses):
            print("----------")
            while True:
                duplicate = False
                course_id = input("Enter course {} ID: ".format(i+1))
                for c in course_information:
                    if course_id == c["ID"]:
                        duplicate = True
                        print("Duplicate course ID. Please re-enter!!!")
                if duplicate == False: 
                    break
            
            course_name = input("Enter course name: ")
            new_course = dict(ID = course_id, Name = course_name, Mark = [])
            print("----------")
            course_information.append(new_course)
        print("Add courses DONE!!!")

    elif option == 3:
        print("Input mark: ")
        while True:    
            course = input("Enter the course: ")
            course_found = False
            for idx, c in enumerate(course_information):
                if course == c["Name"]:
                    course_found = True
                    course_index = idx
                    break
            if course_found == True:
                print("Course found!")
                break
            else:
                print("No course found! Please re-try!")
                    
        print("Enter student's mark: ")
        for student in student_information:
            mark = int(input("{} {} mark: ".format(student["ID"], student["Name"])))
            student["Mark"].append(dict(Course = course, Mark = mark))
            course_information[course_index]["Mark"].append(dict(Student_ID = student["ID"], Student = student["Name"], Mark = mark))
        print("Add courses DONE!!!")        

    elif option == 4:
        print ("Course list: ")
        for c in course_information:
            print("{} - {}".format(c["ID"], c["Name"]))
        print("Display course list DONE!!!") 
        
    elif option == 5:
        print("Student list: ")
        for student in student_information:
            print("ID: {} - Name: {} - DOB: {}".format(student["ID"], student["Name"], student["DOB"]))
        print("Display student list DONE!!!") 

    elif option == 6:
        print("Student's marks for course:")
        course_found = False
        while True:
            course = input("Enter course: ")
            for c in course_information:
                if c["Name"] == course:
                    course_found = True
                    for m in c["Mark"]:
                        print("ID: {} - Student name: {} - Mark: {}".format(m["Student_ID"], m["Student"], m["Mark"]))
                    break
            if course_found == True:
                break
            else:
                print("No course found! Please re-try!")
        print("Display students marks for {} DONE!!!".format(course))     
    
    elif option == 0:
        print ("Exit!!!!")
        break
    
    else:
        print("No option available! Please re-enter!!!")
                
                    


    

