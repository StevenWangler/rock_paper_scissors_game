"""
Rock, Paper, Scissors Game Module.

This module allows a user to play Rock, Paper, Scissors against a "learning" computer opponent.
The computer's strategy revolves around targeting the player's most defeated move, with a slight 
random twist to introduce unpredictability.

Developer: Steven Wangler
"""

import time
import random
from colorama import init, Fore


# Initialize colorama for colorful terminal outputs
init(autoreset=True)


# Constants
MOVES = ['rock', 'paper', 'scissors']
DELIMITER = '~' * 50


# Mapping of moves to the move they defeat
WINNING_COMBINATIONS = {
    'rock': 'scissors',
    'scissors': 'paper',
    'paper': 'rock'
}


# ASCII arts for visual representation of each move
ASCII_ART = {
    'rock': """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    'paper': """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    'scissors': """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
}


def display_intro():
    """Display the introductory message for the game."""
    print(DELIMITER)
    print(Fore.CYAN + 'Welcome to Rock - Paper - Scissors. Can you beat a learning computer?')
    print(Fore.YELLOW + "Press 'R' for Rock, 'P' for Paper, 'S' for Scissors, and 'Q' to quit.")
    print(DELIMITER)


def get_computer_choice(defeat_counts):
    """
    Get computer's choice based on which move has been defeated the most or occasionally at random.
    
    Parameters:
        defeat_counts (dict): A dictionary with counts of how often each move has been defeated.
    
    Returns:
        str: The move chosen by the computer.
    """
    # 30% chance for the computer to choose randomly
    if random.random() < 0.3:
        return random.choice(MOVES)

    most_defeated_move = max(defeat_counts, key=defeat_counts.get)
    return WINNING_COMBINATIONS[most_defeated_move]


def get_player_choice():
    """Get player's move choice."""
    choice = input(Fore.GREEN + "Your move (R/P/S/Q): ").lower()
    return {
        'r': 'rock',
        'p': 'paper',
        's': 'scissors',
        'q': 'quit'
    }.get(choice, 'invalid')


def reveal_choices(player, computer):
    """Display both the player and computer's chosen moves."""
    print("\nRock... Paper... Scissors... SHOOT!\n")
    time.sleep(1)
    print(Fore.BLUE + "You chose:\n" + ASCII_ART[player])
    print(Fore.RED + "Computer chose:\n" + ASCII_ART[computer])


def determine_winner(player_choice, computer_choice):
    """
    Determines the winner based on player and computer choices.
    
    Parameters:
        player_choice (str): The move chosen by the player.
        computer_choice (str): The move chosen by the computer.
    
    Returns:
        str: "tie" if both choices are the same, "player" if player wins, "computer" if computer wins.
    """
    if player_choice == computer_choice:
        return "tie"
    elif WINNING_COMBINATIONS[player_choice] == computer_choice:
        return "player"
    else:
        return "computer"


def main():
    """Main game loop."""
    computer_wins = 0
    human_wins = 0
    ties = 0
    defeat_counts = {'rock': 0, 'paper': 0, 'scissors': 0}
 
    display_intro()

    # Game loop
    while True:
        player_choice = get_player_choice()

        if player_choice == 'quit':
            break
        elif player_choice == 'invalid':
            print(Fore.YELLOW + "Oops! That's not a valid move. Remember, 'R' for Rock, 'P' for Paper, and 'S' for Scissors.")
            continue

        computer_choice = get_computer_choice(defeat_counts)
        reveal_choices(player_choice, computer_choice)

        result = determine_winner(player_choice, computer_choice)
        if result == "tie":
            print(Fore.MAGENTA + "It's a tie!")
            ties += 1
        elif result == "player":
            print(Fore.BLUE + "You've won this round!")
            human_wins += 1
            defeat_counts[computer_choice] += 1
        else:
            print(Fore.RED + "The computer wins this round!")
            computer_wins += 1
            defeat_counts[player_choice] += 1

        print(DELIMITER)
        print(f'{Fore.CYAN}Score:\n{Fore.BLUE}You: {human_wins}\n{Fore.RED}Computer: {computer_wins}\n{Fore.MAGENTA}Ties: {ties}')
        print(DELIMITER)

    print(Fore.CYAN + "Thanks for playing! Here's the final score:")
    print(f'{Fore.BLUE}You: {human_wins} | {Fore.RED}Computer: {computer_wins} | {Fore.MAGENTA}Ties: {ties}')
    print(DELIMITER)


if __name__ == '__main__':
    main()
