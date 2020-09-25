'''
Use this file to write an "open" version of the game (no test code or defined format). This will be translated into a testable program later. Use the reponse statements provided to make that transition easier.

"Your number is too high."
"Your number is too low."
"Your number is out of range."
"I'm sorry you are giving up!"
"I'm sorry, you are out of guesses."

'''

#collaborators: none (Kasey)
print ("we are going to play a guessing number game: ")
print ("press a to reveal the correct answer if you're stuck: ")
range2=int(input("what range do you want the numbers to be? Type the first number here: "))
range3=int(input("Type the second number here: "))
guesses=int(input("how many guesses do you want?: "))

import random
variable = random.randint(range2,range3)


def guess(number1, variable):
        if number1=="a":
            print (f"the number was {variable} ")
        else:
            try:
                number1=int(number1)
                if number1 < variable:
                    print (f"{number1} is too low!")
                elif number1==variable:
                    print (f"{number1} is correct!")
                elif number1 > variable:
                    print (f"{number1} is too high")
            except:
                print("invalid entry")
                
        
        
            

        


for x in range(guesses):
    
    number1=(input("guess a number: "))
    guess(number1, variable)
    
   
   




'''number2=int(input("guess another number"))
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
    print ("Sorry, you are out of guesses")'''


