


from datetime import *

DateOfBirth = datetime.strptime(input("Your birth date (DD.MM.YYYY): "), "%d.%m.%Y")

Age = datetime.now() - DateOfBirth

print(f"You survived {Age.total_seconds()} seconds.")