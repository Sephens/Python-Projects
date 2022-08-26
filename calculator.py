#prompt a user to enter first num number
num1 = input("Enter num one: \n")
# conver num1 to int
num1=int(num1)

#prompt a user to enter an operator
oper = input("Enter operator(+,-,*,/): \n")

#prompt a user to enter second number
num2 = input("Enter second number: \n")
# conver num1 to int
num2=int(num2)

if(oper == "+"):
    ans = num1 + num2
if(oper == "-"):
    ans = num1 - num2
if(oper == "/"):
    ans = num1 / num2
if(oper == "%"):
    ans = num1 % num2
if(oper == "//"):
    ans = num1 // num2
if(oper == "**"):
    ans = num1 ** num2
if(oper == "*"):
    ans = num1 * num2
print("Ans  = ",ans)