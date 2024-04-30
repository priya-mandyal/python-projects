import random

def play():
    user = input("Pick one: 'r' for rock, 's' for scissor, 'p' for paper \n")
    computer = random.choice(['r','p','s'])
    if(has_won(user, computer)):
        print("You lost :(")
        return
    
    print("You won!!! :)")

def has_won(player, opponent):
    if((player == 'r' and opponent == 'p') or (player == 'p' and opponent == 's') or (player == 's' and opponent == 'r')):
        return True
    return False

play()