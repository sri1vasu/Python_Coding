# The greatest ever Rock-Paper-Scissors Championship will take place in your town! The best players will battle each other to see who's the best player in the world. Each player will compete against each other player twice, once home and once away.

# Given the list of the players, your task is to come up with the list of all the games between them, and return them sorted lexicographically.

# Example

# For players = ["trainee", "warrior", "ninja"], the output should be

# solution(players) = [["ninja", "trainee"], ["ninja", "warrior"], 
                              # ["trainee", "ninja"], ["trainee", "warrior"], 
                              # ["warrior", "ninja"],
							  
from itertools import permutations

def solution(players):
    return sorted(list(permutations(players,2)))							  