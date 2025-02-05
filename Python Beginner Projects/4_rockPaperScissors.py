import random 

def is_win(user, computer) :
    #return true if user wins
    #r>s, s>p, p>r
    if (user == 'r' and computer == 's') or \
       (user == 's' and computer == 'p') or \
       (user == 'p' and computer == 'r') :
        return True 
    else :
        return False
    
def play() :
    userMove = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors: ")
    computerMove = random.choice(['r','p','s'])
    print(f'Computer chooses: {computerMove}')

    if userMove == computerMove :
        return 'It\'s a Tie!'
     
    if is_win(userMove, computerMove) :
        return 'You Won!'
    else :
        return 'You lost!'

print(play())