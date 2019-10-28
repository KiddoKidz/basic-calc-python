choice = ''
def add(num1, num2):
    return num1 + num2

def subs(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

def input_checker(item):
    try:
        checked = int(item)
        return True
    except:
        print("Sorry your input is invalid")
        return False

print("Please select operations you want: \n 1. Adding\n 2. Substracting\n 3. Multiplying\n 4. Dividing\n")

while True:
    choice = input("Your choice (1,2,3,4): ")
    if input_checker(choice):
        if choice<1 | choice>4:
            break
        else:
            print("Please input the number in range 1 and 4")


while True:
    num1 = input("Input first number: ")
    num2 = input("Input second number: ")

    if input_checker(num1) & input_checker(num2):
        break

if choice==1:
    print(add(num1,num2))
elif choice==2:
    print(subs(num1,num2))
elif choice==3:
    print(mult(num1,num2))
elif choice==4:
    print(div(num1,num2))
