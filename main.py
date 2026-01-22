import random

def get_computer_choice():
    """Returns a random choice for the computer."""
    choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    return random.choice(choices)

def get_user_choice():
    """Gets and validates the user's choice."""
    while True:
        print("\nChoose your option:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Lizard")
        print("5. Spock")
        print("6. Quit")
        
        user_input = input("\nEnter your choice (1-6): ").strip()
        
        choices_map = {
            '1': 'rock',
            '2': 'paper',
            '3': 'scissors',
            '4': 'lizard',
            '5': 'spock',
            '6': 'quit'
        }
        
        if user_input in choices_map:
            return choices_map[user_input]
        print("Invalid choice. Please enter a number from 1 to 6.")

def determine_winner(user_choice, computer_choice):
    """Determines the winner of the game."""
    if user_choice == computer_choice:
        return "tie"
    
    # Define what each choice beats
    winning_combinations = {
        'rock': ['scissors', 'lizard'],      # Rock crushes Scissors and crushes Lizard
        'paper': ['rock', 'spock'],          # Paper covers Rock and disproves Spock
        'scissors': ['paper', 'lizard'],     # Scissors cuts Paper and decapitates Lizard
        'lizard': ['paper', 'spock'],        # Lizard eats Paper and poisons Spock
        'spock': ['rock', 'scissors']        # Spock vaporizes Rock and smashes Scissors
    }
    
    if computer_choice in winning_combinations[user_choice]:
        return "user"
    return "computer"

def display_result(user_choice, computer_choice, result):
    """Displays the game result."""
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win!")
    else:
        print("Computer wins!")

def main():
    """Main game loop."""
    print("=" * 50)
    print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
    print("=" * 50)
    print("\nRules:")
    print("  Rock crushes Scissors and Lizard")
    print("  Paper covers Rock and disproves Spock")
    print("  Scissors cuts Paper and decapitates Lizard")
    print("  Lizard eats Paper and poisons Spock")
    print("  Spock vaporizes Rock and smashes Scissors")
    print("=" * 50)
    
    user_score = 0
    computer_score = 0
    
    while True:
        user_choice = get_user_choice()
        
        if user_choice == 'quit':
            print(f"\nFinal Score - You: {user_score}, Computer: {computer_score}")
            print("Thanks for playing!")
            break
        
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, result)
        
        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1
        
        print(f"\nScore - You: {user_score}, Computer: {computer_score}")
        print("-" * 40)

if __name__ == "__main__":
    main()