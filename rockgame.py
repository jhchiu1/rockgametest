# Rock, Paper, Scissors game

import random

# Get user input for their name
name = input(' - To begin, what is your name? - \n')

ROCK = 1
PAPER = 2
SCISSORS = 3


# Main loop
def main():

    try:

        # Get player input
        pchoice = getinput()

        # Run through loop unless player choice is q to quit
        while (pchoice != 'q'):

        # Get computer choice   
            cchoice = getcinput()

        # Determine winner
            winner = whowon(int(pchoice), cchoice)

        # Show computer choice
            showcchoice(cchoice)

        # Print winner
            print(winner)

        # Get player choice
            pchoice = getinput()


    except Exception as err:
        print(' An error occurred. Error message: \n', err)

# Display player choice menu, validate input
# Get player input
def getinput():

    while True:

        print('')
        print('ROCK, PAPER SCISSORS GAME!')
        print(' -- Choose 1 as ROCK --')
        print(' -- Choose 2 as PAPER --')
        print(' -- Choose 3 as SCISSORS --')
        print(' - Choose q to Quit -' )
        print('')

        # Get player choice input
        pchoice = input(' Enter a choice: \n')

        # End game if player chooses q to quit
        if (pchoice == 'q'):
            print(' -- End of game! -- \n')
            break


        # Validation to ensure player choice is 1, 2, or 3
        # Display error message if choice invalid
        if (pchoice.isdigit()):
            if (int(pchoice) < 1 or int(pchoice) > 3):
                print(' - ERROR! Choose a number between 1 and 3! - \n')
            else:
                break
        else:
            print(' - ERROR! Choose 1, 2, 3, or q to quit! - \n')

    return pchoice



# Get computer input as random integer of 1, 2, or 3
def getcinput():

    choice = random.randint(1,3)
    return choice


# Loop determines whether player or computer wins, or if tie
def whowon(player, computer):

    if player == computer:
        return "TIE!"

    if (player == ROCK and computer == PAPER):
        return 'Paper beats rock! Computer wins!\n'
    elif (player == ROCK and computer == SCISSORS):
        return 'Rock beats scissors! ' + name + ' WINS!\n'
        score += 1

    if (player == SCISSORS and computer == ROCK):
        return 'Rock beats scissors! Computer wins!\n'
    elif (player == SCISSORS and computer == PAPER):
        return 'Scissors beats paper! ' + name + ' WINS!\n'
        score += 1

    if (player == PAPER and computer == ROCK):
        return 'Paper beats rock! ' + name + ' WINS!\n'
        score += 1
    elif (player == PAPER and computer == SCISSORS):
        return 'Scissors beats paper! Computer wins!\n'


# Show computer's choice
def showcchoice(cchoice):

    if (cchoice == ROCK):
        print('Computer chose: ROCK!\n')
    if (cchoice == PAPER):
        print('Computer chose: PAPER!\n')
    if (cchoice == SCISSORS):
        print('Computer chose: SCISSORS!\n')

if __name__ == '__main__':
    main()


