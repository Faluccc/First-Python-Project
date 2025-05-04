import random

print("Let's play rock, paper, or scissors")
nameinput = input("What ur name: ")

player_wins = 0
computer_wins = 0
tie = 0

while player_wins < 3 and computer_wins < 3:
    player_choice = input("Choose rock, paper, scissors: ").lower()
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "scissors" and computer_choice == "paper") or (player_choice == "paper" and computer_choice == "rock"):
        winner = "Player"
    elif player_choice==computer_choice:
        winner = "Tie"
    else:
        winner = "Computer"

    if winner=="Player":
        print("Luckily you won bruh")
        player_wins += 1

    elif winner=="Computer":
        print(f"Computer won u r dumb {nameinput}😹😹😹😹")
        computer_wins += 1
    else:
        print("It's a tie bruh")
        tie += 1

    print(f"Current Score - {nameinput}: {player_wins}, Computer: {computer_wins}, Tie: {tie}")

if player_wins > computer_wins:
    print(f"wow you won {nameinput}😐.")
    print(f"u won {player_wins} time gg")

elif tie==9:
    print("u such a sussy baka😹")

else:
    print("loser")
    print(f"u Lose {computer_wins} time bruh") 