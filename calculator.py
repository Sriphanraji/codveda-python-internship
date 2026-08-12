# Addition
def add(a,b):
    return a+b

# Subtraction
def subtract(a,b):
    return a-b

# Multiplication
def multiplication(a,b):
    return a*b

# Division
def division(a,b):
    if b==0:
        print("Error :Please enter instead of 'zero' because it causes zerodivision error")
    return(a/b)

# Getting input from user
num1=float(input("Enter First Number :"))
num2=float(input("Enter Second Number :"))

# Displaying Operation to user
print("Select Operations :\n 1.Addition(+)\n 2.Subtraction(-)\n 3.Multiplication(*)\n 4.Division(/)")

# Getting operation input from user
operation=int(input("Enter The Operation Position number :"))

if operation==1:
    print('Addition Result :',add(num1,num2))
elif operation==2:
    print('Subtraction Result :',subtract(num1,num2))
elif operation==3:
    print('Multiplication Result :',multiplication(num1,num2))
elif operation==4:
    print('Division Result',division(num1,num2))
else:
    print("You Entered out from '1 to 4' ,Please Enter the valid operation position :)")

