#rock paper scissors minigame using copilot 
import random

def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, or scissors): ")
    user_choice = user_choice.lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid option. Please choose rock, paper, or scissors.")
        user_choice = input("Enter your choice (rock, paper, or scissors): ")
        user_choice = user_choice.lower()
    return user_choice

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def update_score(result, score):
    if result == "You win!":
        score["user"] += 1
    elif result == "Computer wins!":
        score["computer"] += 1

def print_score(score):
    print(f"User: {score['user']} - Computer: {score['computer']}")

def play_game():
    score = {"user": 0, "computer": 0}

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        update_score(result, score)

        print(result)
        print_score(score)

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

play_game()
