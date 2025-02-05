'''
This is a simple Python game where the user chooses a secret number between user defined lower 
bound and upper bound. Then the computer generates a random number in this bound. And the 
program will tell us whether the computer guesses it correctly or not. The program will guide 
the computer by telling if it's guess is too high or too low. After the  successful guess, it 
will also tell us, how many times the computer tried to solve this game.

To play, simply run the script and follow the on-screen instructions.
Enjoy the game and have fun with computer!
'''

import random 

def computer_guess(secretNumberByUser, l, u):
    low, high = l, u
    cnt = 0 

    print(f"""\n*** Welcome to the Number Guessing Game! ***  
In this game the user chooses a secret number between {low} and {high}.
Then the computer generates a random number in this bound. And the 
program will tell us whether the computer guesses it correctly or not.\n""")
    
    while True :
        try :
            computer_generated_num = random.randint(low, high)
            cnt += 1
            if computer_generated_num > secretNumberByUser :
                print(f'Computer guessed {computer_generated_num}, which is too high!')
                high = computer_generated_num - 1       
            elif computer_generated_num < secretNumberByUser :
                print(f'Computer guessed {computer_generated_num}, which is too low!')
                low = computer_generated_num + 1        
            else :
                print(f'Congratulations! Computer guessed the right number which is {computer_generated_num}, in {cnt} try!')
                return
            
        except ValueError :
            print('Some error occurred!')

        except Exception as e :
            print(f'Error: {e}')
        

def main() :
    try :
        while True :    #keep asking until the valid input is found
            lowerLimit = int(input("Enter the lower limit number: "))
            upperLimit = int(input("Enter the upper limit number: "))

            if lowerLimit == upperLimit :
                print(f'Lower bound and upper bound can not be same!\nPlease Try again!')
            else :
                break

        while True :    #keep asking until the valid input is found
            secretNumberByUser = int(input(f"choose a number between {lowerLimit} to {upperLimit}: "))
            if secretNumberByUser < lowerLimit or secretNumberByUser > upperLimit :
                print(f'Invalid Choice! The secretNumber must be between {lowerLimit} and {upperLimit}')
            else :
                break 
            
        computer_guess(secretNumberByUser,lowerLimit, upperLimit)
        return

    except ValueError :
        print("Invalid Input. Please write an integer as input.")
    
main()