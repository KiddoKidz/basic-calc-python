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

def get_user_inputs():
    while True:
        num1 = input("Input first number: ")
        num2 = input("Input second number: ")

        if input_checker(num1) & input_checker(num2):
            num1 = int(num1)
            num2 = int(num2)
            break
    
    return num1, num2


def main():

    while True:
        print("Please select operations you want: \n 1. Adding\n 2. Substracting\n 3. Multiplying\n 4. Dividing\n 5. Modulo\n 6. Powering")
        choice = input("\nYour choice (1,2,3,4,5,6): ")
        if input_checker(choice):
            choice = int(choice)

            num1, num2 = get_user_inputs()

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
            else:
                print("Choose between 1 - 6!")

            print('\n')


if __name__ == "__main__":
    main()