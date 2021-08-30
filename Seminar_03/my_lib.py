def my_add(x,y):
    return x + y

class Car:
    def __init__(self, speed, m, power, colour, location = "Krasnoyarsk"):
        self.speed = speed
        self.m = m
        self.power = power
        self.colour = colour
        self.location = location
    
    def remove(self, new_location = "Krasnoyarsk"):
        self.location = new_location