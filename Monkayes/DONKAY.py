from Fauna.ANIMAL import Animal
class Donkay(Animal):
    def __init__(self, type_of_monkey, array, age):
        super().__init__("Donkay")
        self.type_of_monkey = type_of_monkey
        self.array = array
        self.age = age
    def infprmation(self):
        return f"this is monkay his type is {self.type_of_monkey}\nhis array is {self.array}"


    def about_himself(self):
        return f"Hi I'm {self.name}\nIm {self.age} years old"