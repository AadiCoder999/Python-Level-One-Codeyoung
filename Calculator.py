def add(num1, num2):
    return num1+num2

def subtract(num1, num2):
    return num1-num2

def multply(num1, num2):
    return num1*num2

def divide(num1, num2):
    return num1/num2

def floordivide(num1, num2):
    return num1//num2

def modulus(num1, num2):
    return num1%num2

def exponent(num1,num2):
    return num1**num2

print("PLAESE SELECT OPERATION \n 1 - Addition \n 2 - Subtraction \n 3 for Multiplication \n 4 - Division \n 5 - Floor Division \n 6 - Remainder \n 7 - Exponent")

choice=int(input("Enter your choice: "))
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))

if(choice==1):
    print("Addition: ",add(num1,num2))

if(choice==2):
    print("Subtraction: ",subtract(num1,num2))

if(choice==3):
    print("Multiplication: ",multply(num1,num2))

if(choice==4):
    print("Division: ",divide(num1,num2))

if(choice==5):
    print("Floor Division: ",floordivide(num1,num2))

if(choice==6):
    print("Remainder ",modulus(num1,num2))

if(choice==7):
    print("Exponent: ",exponent(num1,num2))
    
else:
    print("ERROR ERROR ERROR")
