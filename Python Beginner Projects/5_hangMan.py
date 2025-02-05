import random 
import string

def display_word(cleanWord, guessed_letters):
    # return " ".join([letter if letter in guessed_letters else "_" for letter in cleanWord])

    result = []
    for character in cleanWord : 
        if character in guessed_letters :
            result.append(character)
        else :
            result.append("_")
    return " ".join(result)

def choose_word():
    input_files = 'words.py'

    try:
        with open(input_files, 'r') as readFiles:
            textBlock = readFiles.read()    #read a single string
            WordList = textBlock.split()    #split the single string based on 
            
        computer_choiced_word = random.choice(WordList)     #choose a random word
        cleanWord = computer_choiced_word.strip(string.punctuation).lower()
        return cleanWord

    except FileNotFoundError:
        print(f'The {input_files} file is not found.')

def hangMan():
    word_by_computer = choose_word()
    guessed_letters = set()
    totalAttempts = len(word_by_computer)  #We need at least len(word) times to choose the word
    print(f'\nWelcome to the HangMan Game!')
    
    while totalAttempts > 0:
        try:
            print(f"\nWord: {display_word(word_by_computer, guessed_letters)}")
            guess_a_letter = input(f"Guess a letter: ").lower()

            if len(guess_a_letter) != 1:
                print("Please guess only one letter at a time.")
            elif guess_a_letter in guessed_letters:
                print(f'You already guessed this letter!')
            elif guess_a_letter in word_by_computer:
                guessed_letters.add(guess_a_letter)
                print(f'Correct Guess!\nWord: {display_word(word_by_computer, guessed_letters)}')
            else:
                totalAttempts -= 1
                print(f'Incorrect Attempt. Remaining attempts: {totalAttempts}')

            # Check if the player has won
            # if all(letter in guessed_letters for letter in word_by_computer):
            if set(word_by_computer).issubset(guessed_letters) :
                print(f"Congratulations, you've won! The word was: {word_by_computer}")
                break

        except Exception as explanation:
            print(f"Something wrong happened: {explanation}")

    if totalAttempts == 0:
        print(f"Game Over! The correct word was: {word_by_computer}")

hangMan()
