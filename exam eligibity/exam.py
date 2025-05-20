days = float(input("Enter the amount of working days:  "))
absent = float(input("Enter the amount of days absent:  "))

percentage = (absent / days)*100

print("You have been present for ",int(percentage), "% of the year...")

if percentage <= 74:
    print("You aren't eligible for the exam :(")
else:
    print("You are eligible for the exam :)")