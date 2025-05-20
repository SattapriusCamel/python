def find_factorial(n):
    if n == 1:
        return n
    else:
        return n*find_factorial(n-1)

num= int(input("Type the number that you want to find the factorial of:  "))

if num<0:
    print("Factorials aren't there for negative numbers")
elif num==0:
    print("The Factorial of 0 is 1")
else:
    print("The factorial of ", num, " is ", find_factorial(num))