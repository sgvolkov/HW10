# After you have Version 1 working, you can proceed to implement Version 2, 
# which plays the Seventeen Game in batch mode.

# The program reads from an input file (named 'i206_placein_input.txt') a 
# sequence of comma delimited numbers representing the sequence of moves 
# made by Player 1. Each line of the input file represents a different game. 
# For example, the sample input file contains data for ten games. In the 
# first game, Player 1 removes 3 marbles during its first turn, 1 marble during 
# its second turn, three marbles during its third turn, and so on.

# If the number of marbles left in the jar is fewer than the next number in the 
# play sequence, then Player 1 should remove all the remaining marbles. For 
# example, if there are two marbles left in the jar, and the next number in the 
# sequence is 3, then Player 1 should remove two marbles, not three.
# Player 2 will play the same marble-removal strategy as in Version 1.

# Note that not all numbers in each line may be used, depending on the progress 
# of the game (which in turn depends on the strategy used by Player 2). 
# Conversely, the play sequences are generated such that there will always be 
# enough numbers for each game.

# The program will play the game as many times as there are lines in the input 
# file, printing the sequence of moves and the game winner into an output text 
# file (named i206_placein_output2_<ischool_userid>.txt'), one line per game. 
# At the end of all the games, the program will print the number of games won 
# by each player. See below for what an output file for ten games might look like.

# def open_file():  # opening file into list
#     with open('i206_placein_input_0.txt', 'r') as fin:
#         new_list = fin.read().strip().split('\r\n')

import os
import random

def open_file():  # opening file into list

    large_list = []
    
    f = open("i206_placein_input_0.txt", "r")
    for line in f:
        # This loop will add the list of numbers to large_list
        small_list = []
        
        for letter in line:
            #this loop will add each number to small_list
            try:
                small_list.append(int(letter))
            except:
                continue
        
        large_list.append(small_list)
        
    return large_list
        

def countdown(new_list, current_marbles, turn):
    
    # all play sequences
    play_sequences = []
    game_number = 0
    current_player = ""
    
    for game in new_list:
        
        for human_choice in game:

            # All human actions
            if human_choice > current_marbles:
                human_choice = current_marbles
            
            current_marbles -= human_choice
            #
            
            
            # All computer actions
            
            computer_choice = random.randrange(1,4)
                
            if current_marbles == 3: 
                computer_choice = random.randrange(1,3)
            elif current_marbles == 2:
                computer_choice = random.randrange(1,2)
            elif current_marbles == 1:
                computer_choice = 1
                
            if current_marbles == 0:
                print str(computer_choice)
                print 'Winner: P1.'
                break

            current_marbles -= computer_choice

            # print("Game #" + 1 + ". Play sequence:" + 3-1-1-1-3-1-2-1-3-1 + ". Winner: " + P1 + "\n")
    #Player 1 won 5 times; Player 2 won 5 times.



###############################################################################
def main():

    new_list = open_file()


    countdown(new_list, 17, 0)

if __name__ == '__main__':
    main()