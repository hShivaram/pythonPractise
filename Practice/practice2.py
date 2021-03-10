class Student:
    studentLst=[]
    def __init__(self,id,name,balance):
        self.id=id
        self.name=name
        self.balance=balance
        Student.studentLst.append(self)


for x in range(1,6):
    Student(x,"student"+str(x),x*100)

Student.studentLst