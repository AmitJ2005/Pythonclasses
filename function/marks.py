from gradde import *


firtvalue=(int(input("Enter first value: ")))
secondvalue=(int(input("Enter second value: ")))
thirdvalue=  input("nishaan: ")

if thirdvalue == "+":
    sum_numbers(firtvalue, secondvalue)

elif thirdvalue == "*":
    multiply_numbers(firtvalue, secondvalue)  

elif thirdvalue =="/":
    divide_numbers(firtvalue, secondvalue)

else:
    print("Invalid operation")