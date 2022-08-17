




choose = input("""
    Welcome To The Temperature Unit Converter.
    ------------------------------------------
    1- Celsius to Fahrenheit
    2- Fahrenheit to Celsius
    Which operation do you want to do?

     """)

HowManyEValue = 1

while 0 < HowManyEValue:

    class Converter:

        def __init__(self, C, F):
            self.C = C 
            self.F = F


        def CtoF(self,):
            self.C = input("Enter the value of Celsius: ")
            self.F = ((float(self.C)) * 1.8) + 32
            return self.F

        def FtoC(self):
            self.F = input("Enter the value of Fahrenheit: ")
            self.C = (float(self.F) - 32) / 1.8
            return self.C
    
    if int(choose) == 1:
        con = Converter(0,0)
        print(f"equal to {str(con.CtoF())} degree Fahrenheit.")
    elif int(choose) == 2:
        con = Converter(0,0)
        print(f"equal to {str(con.FtoC())} degree Celsius.")
    else:
        print("Something went wrong!")
    HowManyEValue = HowManyEValue - 1
























































