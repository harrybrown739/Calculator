num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
option = input("multiply, add, divide or subtract")
if option == multiply:
 answer=num1*num2
elif option == add:
 answer=num1+num2
elif option == divide:
 answer=num1/num2
elif option == subtract:
 answer=num1-num2
print(answer)
