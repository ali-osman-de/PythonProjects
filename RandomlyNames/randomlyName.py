
import random

first_names = ["Albert", "Charles", "Nicolas", "Michael", "Anders", "Isaac", "Stephen", "Marie", "Richard"]
last_names = ["Einstein", "Darwin", "Copernicus", "Faraday", "Celsius", "Newton", "Hawking", "Curie","Dawkins"]

def randomlySelect_Name():
    choose_name = random.randint(0,len(first_names))
    name = first_names[choose_name]
    return name

def randomlySelect_Surname():
    choose_surname = random.randint(0,len(last_names))
    surname = last_names[choose_surname]
    return surname

class RandomlyName:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname

    def generate_name(self):
        return (str(self.name) + " " + str(self.surname))

p1 = RandomlyName(randomlySelect_Name(), randomlySelect_Surname())

print(p1.generate_name())






