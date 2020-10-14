#collaborators: Kasey, help from Megan

import random #this imports the random number, depending on the range the user prompts.
       

def guess():
    print ("we are going to play a guessing number game ")
    print ("press a to reveal the correct answer if you're stuck ")
    range2=int(input("what range do you want the numbers to be? Type the first number here: "))
    range3=int(input("Type the second number here: ")) #this area of the code asks the user for their ranges, guesses, and number of guesses
    guesses=int(input("how many guesses do you want?: "))
    variable = random.randint(range2,range3)
    for x in range(guesses):
        number1=(input("guess a number: ")) #this takes in the number of guesses the user wants
        if number1==variable:
            break #if the number is correct, it will stop asking for guesses.
        if number1=="a":
            print (f"the number was {variable} ") #this is the reveal answer feature, if the user is stuck.
        
            
        else:
            try:
                number1=int(number1)
                if number1 < variable:
                    print (f"{number1} is too low!")
                if number1==variable: 
                    print (f"{number1} is correct!") #this area of the code is every possible scenario for each input, either too high, too low, or the right answer.
                    playagain=str(input("Want to play again? Enter y for yes or n for no ")) #this stops the current game if/when the user enters the correct value, and asks the user if they want to play again
                    if playagain=="y":
                        guess()
                    elif playagain=="n":
                        print ("thanks for playing!")
                if number1!=variable and guesses-x==0:
                    variable=str(variable)
                    print ("sorry, out of guesses")
                    playagain2=str(input("Want to play again? Enter y for yes or n for no ")) #this stops the current game if/when the user enters the correct value, and asks the user if they want to play again
                    if playagain2=="y":
                        guess()
                    elif playagain2=="n":
                        print ("thanks for playing!")
                


                elif number1 > variable:
                    print (f"{number1} is too high") 
                
                    
            except:
                print("invalid entry")


        



guess()
    
   
   




