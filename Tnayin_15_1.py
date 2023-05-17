class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("The students name is ", self.name)
        print("The students age is ", self.age)


class Student(Person):
    def __init__(self, name, age, section):
        Person.__init__(self, name, age)
        self.section = section

    def student(self):
        print(f"The students age is {self.age}\nThe students name is {self.name} \nstudent in {self.section} section")


name = input("input students Name:\t")
age = input("input students age:\t")
section = input("input students section:\t")
S = Student(name, age, section)
S.student()

