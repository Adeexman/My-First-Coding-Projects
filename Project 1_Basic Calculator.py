# To build a basic calculator

from math import *

num1 = input("Enter the first number:")
sign = input("Enter arithmetic sign command: ")
num2 = input("Enter the second number:")


if sign == "+":
    result = float(num1) + float(num2)
    print(result)
elif sign == "-" :
    result = float(num1) - float(num2)
    print(result)
elif sign == "/":
    result = float(num1) / float(num2)
    print(result)
elif sign == "*":
    result = float(num1) * float(num2)
    print(result)
elif sign == "^":
    result = pow(float(num1), float(num2))
    print(result)
elif sign == "%":
    result = float(num1) % float(num2)
    print(result)
else:
    print("Error in sign, check the sign you entered - choose from (+ or - or * or / or % or ^).")
    print("Now start the process over")
    sign = input("Enter sign: ")
    num1 = input("Enter number:")
    num2 = input("Enter number:")

    if sign == "+":
        result = float(num1) + float(num2)
        print(result)
    elif sign == "-":
        result = float(num1) - float(num2)
        print(result)
    elif sign == "/":
        result = float(num1) / float(num2)
        print(result)
    elif sign == "*":
        result = float(num1) * float(num2)
        print(result)
    elif sign == "^":
        result = pow(float(num1), float(num2))
        print(result)
    elif sign == "%":
        result = float(num1) % float(num2)
        print(result)




