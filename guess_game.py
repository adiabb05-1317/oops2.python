##guessing index of that 'O'
from random import shuffle
def shuffle_list(list):
    shuffle(list)
    return list


def player_guess():
    guess=''
    while guess not in ['0','1','2']:
        guess=input('enter a guess number in 0,1,2')
        return int(guess)

def check_guess(my_list,guess):
    if my_list[guess]=='O':
        print('its correct guess, WON!!')
    else:
        print('U LOST,WRONG Guess!')  
        print(my_list)  


#initial list
my_list=['','O','']
#shuffle list
mixed_list=shuffle_list(my_list)
#user guess
guess=player_guess()
#checking guess
check_guess(mixed_list,guess)