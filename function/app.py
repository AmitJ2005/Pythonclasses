from functio import *

fistvalue = int(input("Enter first value: "))
secondvalue = int(input("Enter second value: "))
thirdvalue = input("sign ")


if thirdvalue == "+":
    sum_numbers(fistvalue, secondvalue)
elif thirdvalue == "*":
    multiply_numbers(fistvalue, secondvalue)    
elif thirdvalue == "/":
    divide_numbers(fistvalue, secondvalue)  
elif thirdvalue == "-":
    subtract_numbers(fistvalue, secondvalue)
else:
    print("Invalid operation")