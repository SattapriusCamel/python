myage = {'Alex' : 19, 'John Smith' : 80, 'Sam' : 16, 'Abbas' : 30, 'Perrong':42, 'Bird':12, 'Chelu':192}

alexage = int(input("Guess the age of Alex: "))
guesscorrect = 0
if alexage==myage['Alex']:
    print("Good Job!!")
    guesscorrect+=1
else:
    print("Bad Job :(")

johnage = int(input("Now guess John Smith's age:  "))

if johnage==myage['John Smith']:
    print("Good Job!!")
    guesscorrect+=1
else:
    print("Bad Job :(")

samage = int(input("Now guess Sam's age:  "))

if samage==myage['Sam']:
    print("Good Job!!")
    guesscorrect+=1
else:
    print("Bad Job :(")

samage = int(input("Now guess Abbas's age:  "))

if samage==myage['Abbas']:
    print("Good Job!!")
    guesscorrect+=1
else:
    print("Bad Job :(")

samage = int(input("Now guess Perrong's age:  "))

if samage==myage['Perrong']:
    print("Good Job!!")
    guesscorrect+=1
else:
    print("Bad Job :(")
samage = int(input("Now guess Bird's age:  "))

if samage==myage['Bird']:
    print("Good Job!!")
    guesscorrect+=1
else:
    print("Bad Job :(")
samage = int(input("Now guess Chelu's age:  "))

if samage==myage['Chelu']:
    print("Good Job!!")
    guesscorrect+=1
else:
    print("Bad Job :(")
print("Correct Guesses: ", guesscorrect)

