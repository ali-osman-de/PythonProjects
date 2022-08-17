
# Basic Programming with Python

choose = int(input("""
        1- Add
        2- Minus
        3- Divide
        4- Multi
        What is your choose: 
        """))

controller = 5

class mathOperations:
    def __init__(self,number1,number2):
        self.number1 = number1
        self.number2 = number2

    def Add(self):
        numbers = self.number1 + self.number2
        return str(numbers)  

    def Minus(self):
        numbers = self.number1 - self.number2
        return str(numbers)

    def Divide(self):
        try:
            numbers = self.number1 / self.number2
            return str(numbers)
        except ZeroDivisionError:      
            print("A number cannot be divided by zero")
        except:
            print("Something went wrong")

    def Multiple(self):
        numbers = self.number1 * self.number2
        return str(numbers)


while controller > 4:
    if choose > 4:
        print("You entered an invalid transaction! Please try again with a valid transaction!")
        break
    else:
        math = mathOperations(int(input("First Number: ")),int(input("Second Number: ")))
        break


if choose == 1:
    print("The result of the addition operation: " + math.Add())
elif choose == 2:
    print("The result of the subtraction: " + math.Minus())
elif choose == 3:
    print("The result of the division operation: " + math.Divide())
elif choose == 4:
   print("The result of the multiplication operation: " + math.Multiple())


    











