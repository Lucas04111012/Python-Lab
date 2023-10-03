students = []
subjects = []

def showStudents():
    for i in range(len(students)):
        print(i+1,students[i]["name"])
def showSubjects():
    for i in range(len(subjects)):
        print(i+1,subjects[i])
        
def addStudent():
    a = input("Please input new student's name:")
    students.append({"name":a})
    print("Added successfully")
    showStudents()
    
def findStudent():
    print("Find someone")
 
def updateStudentName(idx):
    students[idx]["name"] = input("Please input new name")
    showStudents()
    
def addOrUpdateScore(idx):
    pass

def addSubject():
    a = input("Please input new subject's name:")
    subjects.append(a)
    print("Added successfully")
    showSubjects()
    
def removeSubject():
    showSubjects()
    idx=input("Please input number of subject to remove")
    subjects.pop(int(idx)-1)

def updateSubject():
    showSubjects()
    idx=input("Please input number of subject to update")
    name = input("Please input the new subject name")
    subjects[int(idx)-1] =name
    print("Updated successfully")
    showSubjects()


def processSubject():
    while True:
        print("Subject Management")
        print("1. Add Subject")
        print("2. Remove Subject")
        print("3. Update Subject")
        print("4. return")
        a = input("Please input number 1-4")
        if a == "1":
            addSubject()
        elif a == "2":
            removeSubject()
        elif a == "3":
            updateSubject()
        elif a == "4":
            break
def updateStudent():
    idx = input("Please input the student No.") 
    while True:
        print("1. Modify Name")
        print("2. Add/Modify Subject Score")
        print("3. Remove subject")
        print("4. Return")
        a = input("please input number 1-4")
        if a == "1":
            updateStudentName(int(idx)-1)
        elif a == "2":
            addOrUpdateScore(int(idx)-1)
while True:
    print("Welcome to Student Management System")
    print("1. Add Student")
    print("2. Subject management")
    print("3. Update Student")
    print("4. Quit")
    a = input("Please input a number (1-4)")
    if a == "1":
        addStudent()
    elif a == "2":
        processSubject()
    elif a == "3":
        updateStudent()
    elif a== "4":
        print("See you again")
    print("--------------------------")
