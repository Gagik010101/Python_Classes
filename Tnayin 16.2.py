class Car:
    def __init__(self, name, max_speed):
        self.max_speed = max_speed
        self.name = name

    def __str__(self):
        return f"Name is {self.name}, max speed is {self.max_speed}"

    def advice(self):
        return f"ADVICE\nMake an effort to buy {self.name}"

    def __del__(self):
        print(f"MISSION COMPLETED +")


class BMW(Car):
    def __init__(self, color, year, acceleration):
        super().__init__("BMW_M8", "304 km/h")
        self.color = color
        self.year = year
        self.acceleration = acceleration

    def information(self):
        return f"this car for buysnessmans\nIts value is $136,095"

    def appearance_and_power(self):
        return f"color {self.color}\nYear {self.year}\nacceleration is {self.acceleration} m/s^2"

    def to_buy(self):
        return "opportunity to buy - Unlikely\n"


class Ferrari(Car):
    def __init__(self):
        super().__init__("Ferrari 812 GTS", "339 km/h")


    def information(self):
        return f"this car for millionaires\nIts value is $433,765"



    def to_buy(self):
        return "opportunity to buy - impossible\n"

M8 = BMW("Red", "2023", "11.2")
ferrari = Ferrari()

print(M8)
print(M8.information())
print(M8.appearance_and_power())
print(M8.to_buy())

print(ferrari)
print(ferrari.information())
print(ferrari.to_buy())
print(ferrari.advice())
