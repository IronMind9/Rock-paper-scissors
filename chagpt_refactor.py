import random

def get_player_choice():
    return input("Choose between 'rock', 'scissors', or 'paper':\n")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player, pc):
    if player == pc:
        return "It's a Tie!"
    elif (
        (player == 'rock' and pc == 'scissors') or
        (player == 'scissors' and pc == 'paper') or
        (player == 'paper' and pc == 'rock')
    ):
        return "Player wins!"
    else:
        return "You lose!"

def main():
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()

    print(f"Player chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(player_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    main()
    

