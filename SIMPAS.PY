import random

choices = ['rock', 'paper', 'scissor']

while True:
    print(choices)
    user_choice = input("Enter your choice (or type 'quit' to exit): ").lower()

    if user_choice == "quit":
        print("Game Over")
        break

    if user_choice not in choices:
        print("Invalid choice")
        continue

    computer_choice = random.choice(choices)

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissor") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissor" and computer_choice == "paper")
    ):
        print("You win!")
    else:
        print("Computer wins!")
