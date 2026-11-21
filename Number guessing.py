# import random module to generate random number 
import random 
# computer randomly select number between 1 to 100  
number = random.randint(1,100) 
# Initialised attempts counter 
attempts = 0 
# loop continue until user guess correctly 
while True: 
    guess = int(input("Guess the number:")) 
    attempts = attempts + 1 
    if guess > number: 
        print("Your Guess is too high ! Try Again") 
    elif guess<number: 
        print("Your Guess is too low! Try Again ") 
    else : 
        print("Congratulation ! You Guess the right number .") 
        print("Total Attempts:",attempts) 
        break 
