class school():
    age=0
    name=""
    teacher=""
    house=""
    def __init__(self):
        print("Student info")

    def details(self):
        self.name=input("what is the childs name?")
        self.age=input("how old are they?")
        self.teacher=input("who is their teacher?")
        self.house=input("what house are they in?")
    def display(self):
        print(self.name)
        print(self.age)
        print(self.teacher)
        print(self.house)


student1=school()
student1.details()
student1.display()
student2=school()
student2.details()
student2.display()