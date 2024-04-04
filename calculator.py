
def addition(num1 , num2):
    return num1 + num2


def subtraction(num1 , num2):
    return num1 - num2


def multiplication(num1 , num2):
    return num1 * num2


def divide(num1 , num2):
    if num1 < num2:
        return num2 / num1
    else:
        return num1 / num2


def even_odd(num):
    if num % 2 == 0:
        print(f"Yes {num} is even")
    else:
        print(f"Yes {num} is Odd")




def calucation_fun(first_num, second_num):

    print("+\n-\n*\n/")
    operation = input("Enter the operation:")
    result = ""
    if operation == '+':
        result = addition(first_num, second_num)
    elif operation == '-':
        result = subtraction(first_num, second_num)
    elif operation == '*':
        result = multiplication(first_num, second_num)
    elif operation == '/':
        result = divide(first_num, second_num)

    return result


def input_fun():

    while True:
        first_num = int(input("Enter the first number: "))
        second_num = int(input("Enter the second number: "))

        result = calucation_fun(first_num,second_num)
        print(f"Result of {first_num} and {second_num} is {result}")

        active = True

        while active == True:

            ans = input(f"Continue the operation with {result}? y/n: ")

            if ans == "y":

                next_num = int(input("Enter the next number: "))
                res = result
                result = calucation_fun(result, next_num)
                print(f"Result of {res} and {next_num} is {result}")
            elif ans == "n":
                active = False
                # input(f"Continue the operation with {result}? y/n: ")

input_fun()



