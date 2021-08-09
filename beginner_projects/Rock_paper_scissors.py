import random

def play():
    user = input("choose: 'r' for rock, 'p' for paper, 's' for scissors\n")
    compuuter = random.choice(['r','p','s'])

    if user == compuuter:
        return 'tie'
    if is_win(user, compuuter):
        return 'win'
    return 'lost'
    
def is_win(player, opponent):
    if(player == 'r' and opponent == 's')  or (player == 's' and opponent == 'p')\
        or (player == 'p' and opponent == 'r'):
        return True

print(play())