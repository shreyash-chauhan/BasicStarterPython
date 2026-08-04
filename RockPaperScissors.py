import random
player_score = 0
computer_score = 0
for round in range(5):
    print(f"Round {round + 1}")
    def get_choices():
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        computer_choice = random.choice(["rock", "paper", "scissors"])
        choices = {
            "player": player_choice,
            "computer": computer_choice
        }
        return choices
    choices = get_choices()
    print(choices)
    if choices["player"] == choices["computer"]:
        print("It's a tie!")
    elif (choices["player"] == "rock" and choices["computer"] == "scissors") or \
        (choices["player"] == "paper" and choices["computer"] == "rock")   or \
        (choices["player"] == "scissors" and choices["computer"] == "paper"):
        print("You win!")
        player_score += 1
    else:
        print("Computer wins!")
        computer_score += 1
    print(f"Score - You: {player_score}, Computer: {computer_score}")