def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y

num1 = int(input("Enter number one: "))
num2 = int(input("Enter number two: "))
choice= (input("Enter operation (symbol): "))
if choice=="+":
    print("Sum: ", add(num1, num2))
elif choice=="-":
    print("Difference: ", subtract(num1, num2))
elif choice=="x" or choice=="*": 
    print("Product: ", multiply(num1,num2))
elif choice=="/":
    print("Quotient: ", divide(num1,num2))
