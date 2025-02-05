'''
This is a simple Python game where the computer generates a random number
between 1 and a user-defined upper limit. Your task is to guess the number
correctly. The program will guide you by telling if your guess is too high or too low.
After the successful guess It will also tell you, how many times you have guessed in total.

To play, simply run the script and follow the on-screen instructions.
Enjoy the game and have fun guessing!
'''

import random 

def guess_number(l, u) :
    computer_generated_num = random.randint(l, u) 
    count = 0

    print(f"""\n*** Welcome to the Number Guessing Game! ***  
In this game the computer generates a random number between {l} and 
{u}. And you have to guess a number between {l} and {u} and the 
program will tell you whether your guess is correct or not.""")
    
    while True : 
        try :
            guess_a_number = int(input(f"Guess a number between {l} and {u}: "))
            count += 1

            if guess_a_number > computer_generated_num :
                print(f'Sorry! You guessed too high. Guess again!')
            elif guess_a_number < computer_generated_num :
                print(f'Sorry! You guessed too low. Guess again!')
            else :
                print(f"Yahoooo! You guessed it right! Congrats to you!")
                print(f"Your total try is: {count} times")
                exit()

        except ValueError :
            print("Please guess an int number!")


def main() :
    try: 
        lowerLimit = int(input("Set the lower limit to guess the number: "))
        upperLimit = int(input("Set the upper limit to guess the number: "))
        guess_number(lowerLimit, upperLimit)

    except ValueError :
        print(f'Invalid Input. Please Enter an Integer.')

main()