class Student:
    def __init__(self,name,id,cls) -> None:
        self.name=name
        self.id=id
        self.cls=cls
    def __repr__(self) -> str:
        return f'Student name : {self.name}, class : {self.cls}, id : {self.id}'
class Teacher:
    def __init__(self,name,subject,id) -> None:
        self.name=name
        self.subject=subject
        self.id=id
    def __repr__(self) -> str:
        return f'Teacher name : {self.name}, Subject : {self.subject}'
class School:
    def __init__(self,name) -> None:
        self.name=name
        self.teacher=[]
        self.student=[]
    def add_teacher(self,name,subject):
        id=len(self.teacher)+101
        teacher=Teacher(name,subject,id)
        self.teacher.append(teacher)
    def enroll(self,name,fee):
        if fee<6500:
            print("Not Enough Money")
        else:
            id=len(self.student)+1
            student=Student(name,id,'C')
            self.student.append(student)
            print(f'Your are enrolled {name} extra money: {fee-6500}')
    def __repr__(self) -> str:
        print(f'Welcome To {self.name}')
        print("---------Our Teacher-----------")
        for teacher in self.teacher:
            print(teacher)
        print("----------Our Student----------")
        for student in self.student:
            print(student)
        return "All for Now"
phitron = School('Phitron')
phitron.add_teacher('Rahat','C')
phitron.add_teacher('Rahim','DSA')
phitron.add_teacher('Fahad','Algo')
phitron.enroll('Mini',6500)
phitron.enroll('Tom',8000)
phitron.enroll('Jerry',9000)
print(phitron)