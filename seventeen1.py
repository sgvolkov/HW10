# # After you have Version 1 working, you can proceed to implement Version 2, 
# which plays the Seventeen Game in batch mode.
# # The program reads from an input file (named 'i206_placein_input.txt') a 
# sequence of comma delimited numbers representing the sequence of moves made 
# by Player 1. Each line of the input file represents a different game. For 
# example, the sample input file contains data for ten games. In the first game,
#  Player 1 removes 3 marbles during its first turn, 1 marble during its second 
#  turn, three marbles during its third turn, and so on.

# # If the number of marbles left in the jar is fewer than the next number in the 
# play sequence, then Player 1 should remove all the remaining marbles. For 
# example, if there are two marbles left in the jar, and the next number in 
# the sequence is 3, then Player 1 should remove two marbles, not three.
# # Player 2 will play the same marble-removal strategy as in Version 1.

# # Note that not all numbers in each line may be used, depending on the 
# progress of the game (which in turn depends on the strategy used by Player 2). 
# Conversely, the play sequences are generated such that there will always be enough 
# numbers for each game.

# # The program will play the game as many times as there are lines in the input 
# file, printing the sequence of moves and the game winner into an output text file 
# (named i206_placein_output2_<ischool_userid>.txt'), one line per game. At the 
# end of all the games, the program will print the number of games won by each 
# player. See below for what an output file for ten games might look like.


#Import
 
import random

#Body

print "\nLet's play the game of Seventeen!"
print "Number of marbles left in jar: 17"

def countdown(current_marbles, turn):
    if turn == 0:  # human's turn = 0
        human_choice = raw_input('\nYour turn: How many marbles will you remove (1-3)? ')
        if type(human_choice) is int:
            if human_choice in range(1,4):  # if human chooses between 1-3, which is correct
                current_marbles = current_marbles - human_choice
                if current_marbles == 0:  # if there are no marbles left, you lose
                    print '\nThere are no marbles left. Computer wins!'
                    return
                elif current_marbles >= 1:
                    print "\nYou removed " + str(human_choice)
                    print "Number of marbles left in jar: " + str(current_marbles)
                    turn = 1
                    countdown(current_marbles, turn)
        else:  # if they don't pick a number between 1-3, they need to try again
            print '\nSorry, that is not a valid option. Try again!'
            countdown(current_marbles, turn)
    else: 
        if turn == 1:  # computer's turn = 1
            print "\nComputer's turn..."
            if current_marbles > 3:
                computer_choice = random.randrange(1,4)  # 
            elif current_marbles == 3:  # if there are 3 marbles left, computer
            # shouldn't choose 3, or it will lose. Same logic applies below
                computer_choice = random.randrange(1,3)
            elif current_marbles == 2:
                computer_choice = random.randrange(1,2)
            elif current_marbles == 1:
                computer_choice = 1
            current_marbles = current_marbles - computer_choice
            if current_marbles == 0:
                print "Computer removed " + str(computer_choice) + " marbles."
                print '\nThere are no marbles left. You win!'
                return
            print "Computer removed " + str(computer_choice) + " marbles."
            print "Number of marbles left in jar: " + str(current_marbles)
            turn = 0
            countdown(current_marbles, turn)

###############################################################################
def main():   
    countdown(17, 0)

if __name__ == '__main__':
    main()