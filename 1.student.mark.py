from prettytable import PrettyTable

listStudent = []
ListCourse =[]

#Students: 
def Student():
    noStudent = int(input("Enter number of students:"))
    for x in range(noStudent):
        print("Student no."+str(x+1)+":")
        id = input("\tID: ")
        name = input("\tName: ")
        dob = input("\tDate of birth: ")
        # 1 student is 1 dict
        dictStudent={'ID':id, 'Name': name, 'DOB':dob}
        # add to student list
        listStudent.append(dictStudent)

#show list of students
def showListStudents():
    studentsTable = PrettyTable()
    studentsTable.field_names = ["Student ID", "Name", "DOB"]
    for i in listStudent:
        studentsTable.add_row([i["ID"],i["Name"],i["DOB"]])
    print(studentsTable)
       
#courses
def Course():
    noCourse = int(input("Enter number of courses:"))
    for x in range(noCourse):
        print("Course no."+str(x+1)+":")
        id = input("\tID: ")
        name = input("\tName: ")
        # 1 course is 1 dict
        dictCourse={'ID':id, 'Name': name }
        # add to course list
        ListCourse.append(dictCourse)

#show list of course
def showListCourses():
    coursesTable = PrettyTable()
    coursesTable.field_names = ["Course ID", "Name"]
    for course in ListCourse:
        coursesTable.add_row([course["ID"],course["Name"]])
    print(coursesTable)

#add mark
def addMarks():
    for i in ListCourse:
        i["mark"]=[]
        for x in listStudent:
            markOfStu = input("Enter mark of courseID " + i['ID'] +" for student "+ x["Name"] +":")
            dictMark={"Student name": x['Name'], "Mark" : markOfStu}
            i["mark"].append(dictMark)
    print("----------------------------------------------")

#show mark
def showMarks():
    for i in ListCourse:
        print("CourseID " + i['ID'] + ":" )
        for x in i["mark"]:
            print("\t" +x["Student name"]+":\t"+x["Mark"])


#main
while(True):
    print("Options:")
    print(" 1.Add students\n 2.Show list of students\n 3.Add courses\n 4.Show list of courses\n 5.Enter marks\n 6.Show marks for courses\n 7.Exist")
    choice= int(input("PLease enter your choice: "))
    print("----------------------------------------------")
    if (choice == 1):
        Student()
        print("----------------------------------------------")
    elif (choice == 2):
        print("-> Here is the students'list")
        showListStudents()
        print("----------------------------------------------")
    elif (choice == 3):
        Course()
        print("----------------------------------------------")
    elif (choice == 4):
        print("-> Here is the courses'list")
        showListCourses()
        print("----------------------------------------------")    
    elif (choice == 5):
        if (len(listStudent)==0 | len(ListCourse)==0):
            print('Lack info of students or courses')
            print("----------------------------------------------")
            continue
        else:
            addMarks()
            print("----------------------------------------------")
    elif (choice == 6):
        print("-> Here is the marks'list")
        showMarks()
        print("----------------------------------------------")
    else:
        break

