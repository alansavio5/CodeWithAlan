import random

while True:
    choices = ["rock","paper","scissors"]
    player = None
    computer = random.choice(choices)

    while player not in choices:
        player = input("rock, paper, or scissors? ").lower()
        if player == computer:
            print(f"Player: {player}")
            print(f"Computer: {computer}")
            print("Tie")

        elif player == "rock":
            if computer == "paper":
                print(f"Player: {player}")
                print(f"Computer: {computer}")
                print("You Lose")

            elif computer == "scissors":
                print(f"Player: {player}")
                print(f"Computer: {computer}")
                print("You Win")

        elif player == "paper":
            if computer == "rock":
                print(f"Player: {player}")
                print(f"Computer: {computer}")
                print("You Win")

            elif computer == "scissors":
                print(f"Player: {player}")
                print(f"Computer: {computer}")
                print("You Lose")

        elif player == "scissors":
            if computer == "rock":
                print(f"Player: {player}")
                print(f"Computer: {computer}")
                print("You Lose")

            elif computer == "paper":
                print(f"Player: {player}")
                print(f"Computer: {computer}")
                print("You Win")

    play_again = input("Do You want to play again? (yes/no) ").lower()
    if play_again != "yes":
        break

print("Have a nice day")