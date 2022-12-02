# The Elves begin to set up camp on the beach. To decide whose tent gets to be closest to the snack storage, a giant Rock Paper Scissors tournament is already in progress.

# Rock Paper Scissors is a game between two players. Each game contains many rounds; in each round, the players each simultaneously choose one of Rock, Paper, or Scissors using a hand shape. Then, a winner for that round is selected: Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. If both players choose the same shape, the round instead ends in a draw.

# Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) that they say will be sure to help you win. "The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.

# The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.

# The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

# Since you can't be sure if the Elf is trying to help you or trick you, you should calculate the score you would get if you were to follow the strategy guide.

# For example, suppose you were given the following strategy guide:

# A Y
# B X
# C Z
# This strategy guide predicts and recommends the following:

# In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
# In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
# The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
# In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

# What would your total score be if everything goes exactly according to your strategy guide?

# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors.
# (0 if you lost, 3 if the round was a draw, and 6 if you won).
# 1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won)
def game(input):
    #opponent rock
    if input[0] == 'A':
        #rock
        if input[2] == 'X':
            return 3+1
        #paper
        elif input[2] == 'Y':
            return 6+2
        #scissors
        elif input[2] == 'Z':
            return 0+3
    # opponent paper
    if input[0] == 'B':
        #rock
        if input[2] == 'X':
            return 0+1
        #paper
        elif input[2] == 'Y':
            return 3+2
        #scissors
        elif input[2] == 'Z':
            return 6+3
    # opponent scissors
    if input[0] == 'C':
        #rock
        if input[2] == 'X':
            return 6+1
        #paper
        elif input[2] == 'Y':
            return 0+2
        #scissors
        elif input[2] == 'Z':
            return 3+3

# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
def game2(input):
    #opponent rock
    if input[0] == 'A':
        #rock
        #need to lose
        if input[2] == 'X':
            return 0+3
        #paper
        #need to tie
        elif input[2] == 'Y':
            return 3+1
        #scissors
        #need to win
        elif input[2] == 'Z':
            return 6+2
    # opponent paper
    if input[0] == 'B':
        #rock
        #need to lose
        if input[2] == 'X':
            return 0+1
        #paper
        #need to tie
        elif input[2] == 'Y':
            return 3+2
        #scissors
        #need to win
        elif input[2] == 'Z':
            return 6+3
    # opponent scissors
    if input[0] == 'C':
        #rock
        #need to lose
        if input[2] == 'X':
            return 0+2
        #paper
        #need to tie
        elif input[2] == 'Y':
            return 3+3
        #scissors
        #need to win
        elif input[2] == 'Z':
            return 6+1

with open('input2.txt') as input:
    score = 0
    for lines in input:
        score+=int(game2(lines))
    print(score)
