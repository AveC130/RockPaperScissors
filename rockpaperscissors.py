'''
Made By: AveC130
Game of Rock Paper Scissors
Made: 11/15/2026
'''

#Allow for computer() to choose between Rock, paper, or scissors
import random

#brings everything together
def main():
    '''
    Introduction to the game and keeps track of points
    while displaying if the user won or not, and the computer choice.
    Also asks if the user wants to play again.
    '''
    print('Welcome To The Game Of Rock Paper Scissors!')
    print('-------------------------------------------')

    point = 0

    while True:
        user = human()
        pick = computer()
        result = results(user, pick)
        point = score(point, result)

        print(f'The Computer Chose: {pick} | {result}')
        print(f'Score: {point}')
        print()

        play_again = input('Would you like to play again? (type "no" to stop): ').strip().lower()


        if play_again == 'no':
            print(f'You finished with {point} points.')
            print('Thanks for playing!')
            break


#Keeps track of the score
def score(point, result):
    '''
    If the user won the score increase by one.
    '''
    if result == 'You win!':
        point += 1
    return point

#Keeps track of users choice
def human():
    '''
    Asks the user for their choice only when they write
    the correct options, otherwise the user will be asked
    to choose again.
    '''
    user = input('Enter your choice (rock, paper, scissors): ').strip().lower()

    while True:
        if user in ['rock', 'paper', 'scissors']:
            return user
        else:
            print()
            print('Please enter rock, paper, or scissors only!')
            user = input('Enter your choice (rock, paper, or scissors): ').strip().lower()

#Keeps track of the computers choice
def computer():
    '''
    Randomly chooses an option from rock paper scissors.
    '''
    choice = ['Rock', 'Paper', 'Scissors']
    pick = random.choice(choice).lower()
    return pick

#decides if the user has won, lost, or tied
def results(user, pick):
    '''
    Calculates to see if the user won or not through
    the users and computers choice.
    '''
    if user == pick:
        return 'Tie!'
    elif user == 'rock' and pick == 'scissors':
        return 'You win!'
    elif user == 'paper' and pick == 'rock':
        return 'You win!'
    elif user == 'scissors' and pick == 'paper':
        return 'You win!'
    else:
        return 'You lose!'

#displays everything in this file
if __name__ == '__main__':
    main()
