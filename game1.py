'''
Use this file to write an "open" version of the game (no test code or defined format). This will be translated into a testable program later. Use the reponse statements provided to make that transition easier.

"Your number is too high."
"Your number is too low."
"Your number is out of range."
"I'm sorry you are giving up!"
"I'm sorry, you are out of guesses."

'''

#collaborators: none (Kasey)

import random
variable = random.randint(0, 10)
try:
    number1=int(input("guess a number"))


    if number1 < variable:
        print (f"{number1} is too low!")
    elif number1==variable:
        print (f"{number1} is correct!")
    elif number1> variable:
        print (f"{number1} is too high")

    number2=int(input("guess another number"))
        if number2 < variable:
        print (f"{number2} is too low!")
    elif number2==variable:
        print (f"{number2} is correct!")
    elif number2 > variable:
        print (f"{number2} is too high")

    number3=int(input("guess another number"))
    if number3 < variable:
        print (f"{number3} is too low!")
    elif number3==variable:
        print (f"{number3} is correct!")     
    elif number3 > variable:
        print (f"{number3} is too high")

    number4=int(input("guess another number"))
    if number4 < variable:
        print (f"{number4} is too low!")
    elif number4==variable:
        print (f"{number4} is correct!")
    elif number4> variable:
        print (f"{number4} is too high")

    number5=int(input("guess another number"))
    if number5 < variable:
        print (f"{number5} is too low!")
    elif number5==variable:
        print(f"{number5} is correct!")
    elif number5> variable:
        print (f"{number5} is too high")
    if  number1 or number2 or number3 or number5 != variable:
        print ("Sorry, you are out of guesses")


