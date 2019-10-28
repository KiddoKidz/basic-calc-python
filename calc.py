choice = ''
def add(num1, num2):
    return num1 + num2

def subs(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def subs(num1, num2):
    return num1 / num2

def input_checker(item):
    try:
        checked = int(item)
        choice = checked
        return True
    except:
        print("Sorry your input is invalid")
        return False

print("Please select operations you want: \n 1. Adding\n 2. Substracting\n 3. Multiplying\n 4. Dividing\n")

choice = input("Your choice (1,2,3,4): ")
while True:
    choice = input("Your choice (1,2,3,4): ")
    if input_checker(choice):
        break

