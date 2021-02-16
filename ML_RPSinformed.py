# HW 1
# ML for rock, Paper, Scissor
# Sahil Sharma
# U4471145
# sahils57@bu.edu
""" the idea of th ealgorithm below is to beat the hand that the computer will use to bat the predicted hand of the user
    for this to happen it is important to know the thinking process of the computer, after playing afew hands with the computer
    I realised that the computer tries to find patterns in my play starting with pattern of 4 if none of 4 are found it tries
    to find patterns of 3 and then 2 and so on. If a certain pattern is foundin my play hitory it takes the next hand in the
    history list to be my next move. In the case that  the pattern is found multiple times, the computer finds the most
    prominent next move to that particular pattern and then using this idea the computer chooses a hand that would defeat
    my predicted hand. I use a imilar method to find my next predicted move and then use that to find the computers next move
    and then play the hand that would beat the computer. this is all done in the novice play.
    """


""" the program runs as a user interface where the user is asked if they want to play another hand if they do they are asked
    to enter the computer's alst play, this done so to calculate the score or incase further development of teh programm is required.
    After the algorithm figures out the best player hand is tell the user using a print statement where
    'r' stands for rock
    'p' stands for paper
    's' stands for scissor
    """

""" for the first turn the player is asked to start with scissors while random play is suggested for the first 5 moves
    """
    
import random

def r_p_s():
    comp_data_base = []         # record of each move of the computer
    comp_score_card = []        # scorecard of computer
    
    
    
    count = 0         # number of moves that have taken place
    print(" start with Scissors, it is statistically the best intial move" )
    
    player_data_base = ['s']        # record of players moves
    player_score_card = []       # scores of player that help the computer predict

    
    to_play = input("another turn? 'y'/'n'")      # asking the palyer if they want to play

    
    while to_play != 'y' and to_play != 'n':
        """ ask the player to enter either 'n' or 'y' """
        to_play = input("another turn? 'y'/'n'")

    #keep the loop that runs the algorithm going till the player doesn't want to play anymore
    while to_play != 'n':
        count += 1                      # to keep the count of how many hands have been played          
        last_comp_play = input("Enter computer's last play ('r'/'p'/'s') : ")
        comp_data_base += last_comp_play        # update database
        score_update(player_data_base[-1] , comp_data_base[-1], player_score_card, comp_score_card)


        if count < 5:
            """ play random for the first 5 turns """
            new_play = play_random()

        else:
            """ execution of the algorithm """
            pat_array = pattern(player_data_base, 4)    # this produces al the next hands for a certain pattern 
            
            pob_pair_array_pat = [max_pair_prob(pat_array, 'r'), max_pair_prob(pat_array, 'p'), max_pair_prob(pat_array, 's')] # this next step produces an array that has a maximum probability pairs of a certain pattern
            max_pair = max(pob_pair_array_pat)                   # getting the pair of maximum probability
            predicted_play = max_pair[1]                 # getting the hand with the maximum probability
            new_play = beat(beat(predicted_play))        # using function beat twice to beat the computer
            



        player_data_base += [new_play]    # updating the database of hands played by the player 
        print(" next move should be ", new_play )
        to_play = input("another turn? 'y'/'n'")
        
        
    
    


def score_update(player_move, robot_move, player_score_card, comp_score_card):
    """ this is unused but was meant to update score in case latest score was used in prediction """
    win_cases = [['r', 's'], ['p', 'r'], ['s', 'p']]
    draw_cases = [['r', 'r'], ['p', 'p'], ['s', 's']]
    current_pair = [player_move, robot_move]
    if current_pair in win_cases:
        comp_score_card += [-1]
        player_score_card += [1]

    elif current_pair in draw_cases:
        comp_score_card += [0]
        player_score_card += [0]

    else:
        comp_score_card += [1]
        player_score_card += [-1]


def play_random():
    """ choses a random hand for the player """
    base_array = [ 'r', 'p', 's' ]
    
        
    initial_random_tries = random.randint(0, 2)
    initial_random_tries = random.randint(0, 2)

    return base_array[initial_random_tries]




def pattern(player_data_base, num_to_look):
    ''' check the last three for the pattern '''
    
    num_end = -1*num_to_look
    last_pattern = player_data_base[num_end::]
    
    next_in = []
    while next_in == []:
        last_pattern = player_data_base[num_end::]
        for i in range(len(player_data_base) - num_to_look):
            
            to_comp = player_data_base[i:i+num_to_look]
            if to_comp == last_pattern:
                next_in += [player_data_base[i+num_to_look]]

        num_end += 1
        num_to_look -= 1
        
    return next_in


                       


def max_pair_prob(array, hand):
                        
    ''' RETURNs the probability of each hand with the hand itself '''
    num_of_hand = 0
    # for  hand
    length_array = len(array)
    if length_array == 0:
        return [0, hand]
    for i in range(len(array)):
        if array[i] == hand:
            num_of_hand += 1
    prob_hand = num_of_hand/length_array
    return [prob_hand, hand]
        

    
    
def beat(move):
    ''' returns the hand that will beat the input move '''
    if move == 'r':
        return 'p'
    elif move == 's':
        return 'r'
    else:
        return's'

