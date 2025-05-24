number1 =  int(input("Enter a value:  "))

numbersum= 0

number2 = number1
while number2 > 0:
    number = number2 % 10
    numbersum += number ** 3
    number2 //= 10

if number1 == numbersum:
    print("The sum of all of them cubed is: ",numbersum)
    print(number1, " Is an armstrong number")
else:
    print("The sum of all of them cubed is: ",numbersum)
    print(number1, " Is NOT an armstrong number")