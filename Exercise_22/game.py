#!/usr/bin/env python3

"""
    This code implements the Rock-Paper-Scissor game
"""

def rpsWinner(move1, move2):
    """
        This function returns the winner of the game or tie
    """
    if move1 == "rock" and move2 == "scissors" \
        or move1 == "scissors" and move2 == "paper" \
        or move1 == "paper" and move2 == "rock":
        return "player one"
    elif move1 == "rock" and move2 == "paper" \
        or move1 == "paper" and move2 == "scissors" \
        or move1 == "scissors" and move2 == "rock":
        return "player two"
    else:    
        return "tie"


# main code
assert rpsWinner('rock', 'paper') == 'player two'
assert rpsWinner('rock', 'scissors') == 'player one'
assert rpsWinner('paper', 'scissors') == 'player two'
assert rpsWinner('paper', 'rock') == 'player one'
assert rpsWinner('scissors', 'rock') == 'player two'
assert rpsWinner('scissors', 'paper') == 'player one'
assert rpsWinner('rock', 'rock') == 'tie'
assert rpsWinner('paper', 'paper') == 'tie'
assert rpsWinner('scissors', 'scissors') == 'tie'
