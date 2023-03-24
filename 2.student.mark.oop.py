from prettytable import PrettyTable

ListStudent=[]
ListCourse= []

class Student:
    def __init__(self, StudentID, StudentName, StudentDOB):
        self._StudentID= StudentID
        self._StudentName = StudentName
        self._StudentDOB = StudentDOB

    def get_studentID(self):
        return self._StudentID
    
    def get_studentName(self):
        return self._StudentName
    
    def get_studentDOB(self):
        return self._StudentDOB
    
class Course:
    def __init__(self,courseID, courseName):
        self.courseID = courseID
        self.courseName = courseName
        self.__mark=[]
    
    def get_courseID(self):
        return self.courseID
    
    def get_courseName(self):
        return self.courseName
    
    def set_marks(self, studentName, mark):
        self.__mark.append({"Student name":studentName, "Mark": mark })

    def get_marks(self):
        return self.__mark

def add_student():
    noStudent = int(input("Enter number of students:"))
    for x in range(noStudent):
        print("Student no."+str(x+1)+":")
        id = input("\tID: ")
        name = input("\tName: ")
        dob = input("\tDate of birth: ")
        stu=Student(id,name,dob)
        ListStudent.append(stu)
    
def showListStudents():
    studentsTable = PrettyTable()
    studentsTable.field_names = ["Student ID", "Name", "DOB"]
    for i in ListStudent:
        studentsTable.add_row([i.get_studentID(), i.get_studentName(), i.get_studentDOB()])
    print(studentsTable)

def add_course():
    noCourse = int(input("Enter number of courses:"))
    for x in range(noCourse):
        print("Course no."+str(x+1)+":")
        id = input("\tID: ")
        name = input("\tName: ")
        # 1 course is 1 dict
        course=Course(id,name)
        # add to course list
        ListCourse.append(course)

def showListCourses():
    coursesTable = PrettyTable()
    coursesTable.field_names = ["Course ID", "Name"]
    for i in ListCourse:
        coursesTable.add_row([i.get_courseID(), i.get_courseName()])
    print(coursesTable)                

def addMarks():
    for i in ListCourse:
        print("Enter mark of courseID " +i.get_courseID()+":")
        for x in ListStudent:
            markOfStu = input("\t" + x.get_studentName() + ":\t")
            i.set_marks(x.get_studentName(),markOfStu)

def showMarks():
    for i in ListCourse:
        print("CourseID " + i.get_courseID() + ":" )
        for x in i.get_marks():
            print("\t" + x["Student name"]+":\t"+x["Mark"])


#main
while(True):
    print("Options:")
    print(" 1.Add students\n 2.Add courses\n 3.Enter marks\n 4.Show list of students\n 5.Show list of courses\n 6.Show marks for courses\n 7.Exist")
    choice= int(input("PLease enter your choice: "))
    print("----------------------------------------------")
    if (choice == 1):
        add_student()
        print("----------------------------------------------")
    elif (choice == 2):
        add_course()
        print("----------------------------------------------")
    elif (choice == 3):
        if (len(ListStudent)==0 | len(ListCourse)==0):
            print('Lack info of students or courses')
            print("----------------------------------------------")
            continue
        else:
            addMarks()
            print("----------------------------------------------")
    elif (choice == 4):
        print("-> Here is the students'list")
        showListStudents()
        print("----------------------------------------------")
    elif (choice == 5):
        print("-> Here is the courses'list")
        showListCourses()
        print("----------------------------------------------")    
    elif (choice == 6):
        print("-> Here is the marks'list")
        showMarks()
        print("----------------------------------------------")
    else:
        break
