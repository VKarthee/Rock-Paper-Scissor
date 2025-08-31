import random

print("Greetings User!!!\nWelcome to Rock, Paper, Scissors!")
print("Type rock, paper, or scissors to play.")
print("Type 'score' to see the score or 'quit' to stop.\n")
print("GOOD LUCK!!!\n")

player_score = 0
computer_score = 0
draws = 0

while True:
    player = input("Your move: ").lower()

    if player == "quit":
        break
    if player == "score":
        print(f"=====Score========\nYou: {player_score} | Computer: {computer_score}\n==================\n")
        continue
    if player not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please type rock, paper, or scissors.\n")
        continue

    computer = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer}")

    if player == computer:
        print("It's a draw!\n")
        draws += 1
    elif (player == "rock" and computer == "scissors") \
        or (player == "scissors" and computer == "paper") \
        or (player == "paper" and computer == "rock"):
        print("You win this round!\n")
        player_score += 1
    else:
        print("Computer wins this round!\n")
        computer_score += 1

    print(f"=====Score========\nYou: {player_score} | Computer: {computer_score} | Draws: {draws}\n==================\n")

print("\nGame Over!")
print(f"======Final Score=========\nYou: {player_score} | Computer: {computer_score}| Draws: {draws}\n==========================\n")
print("\nThanks for playing!")
