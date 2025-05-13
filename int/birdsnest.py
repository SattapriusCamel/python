num = int(input("Enter a number:  "))

if num>50:
    print("Number is greater than 50")
    if num%2==0:
        print("And it is even too")
    else:
        print("And it's odd...")

else:
    print("Number is less than 50")