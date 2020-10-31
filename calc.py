choice = ''
def add(num1, num2):
    return num1 + num2

def subs(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

def mod(num1, num2):
    return num1 % num2

def power(num1, num2):
    result = 1
    for i in range(num2):
        result *= num1
    return result

def input_checker(item):
    try:
        checked = int(item)
        return True
    except:
        print("\nSorry your input is invalid")
        return False

def main():

    print("Please select operations you want: \n 1. Adding\n 2. Substracting\n 3. Multiplying\n 4. Dividing\n 5. Modulo\n 6. Powering")

    while True:
        choice = input("\nYour choice (1,2,3,4,5,6): ")
        if input_checker(choice):
            choice = int(choice)
            if choice<1 or choice>6:
                print("\nPlease input the number in range 1 and 6")
            else:
                break


    while True:
        num1 = input("Input first number: ")
        num2 = input("Input second number: ")

        if input_checker(num1) & input_checker(num2):
            num1 = int(num1)
            num2 = int(num2)
            break

    if choice==1:
        print(num1, "+", num2, " = ", add(num1,num2))
    elif choice==2:
        print(num1, "-", num2, " = ", subs(num1,num2))
    elif choice==3:
        print(num1, "*", num2, " = ", mult(num1,num2))
    elif choice==4:
        print(num1, "/", num2, " = ", div(num1,num2))
    elif choice==5:
        print(num1, "%", num2, " = ", mod(num1,num2))
    elif choice==6:
        print(num1, "^", num2, " = ", power(num1,num2))