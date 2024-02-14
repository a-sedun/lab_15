import random

# Можливі дії: 0 - Rock, 1 - Paper, 2 - Scissors
ACTIONS = {0: "Rock", 1: "Paper", 2: "Scissors"}

# Перемоги для кожного варіанту
VICTORIES = {
    "Rock": "Scissors",  # Rock beats scissors
    "Paper": "Rock",  # Paper beats rock
    "Scissors": "Paper",  # Scissors beats paper
}


def get_user_selection(actions: dict) -> str:
     # Побудова рядка для виведення варіантів вибору користувача
    choices = [f"{actions[action]}[{action}]" for action in actions]
    choices_str = ", ".join(choices)
     # Отримання вибору користувача
    selection = int(input(f"Enter a choice ({choices_str}): "))
    action = actions[selection]
    return action


def get_computer_selection(actions: dict) -> str:
    # Випадковий вибір дії для комп'ютера
    selection = random.randint(0, len(actions) - 1)
    action = actions[selection]
    return action


def get_determine_winner(victories: dict, user_action: str, computer_action: str) -> str:
     # Визначення переможця на основі введених дій гравця та комп'ютера
    defeats = victories[user_action]
    if user_action == computer_action:
        result = f"Both players selected {user_action}. It's a tie!"
    elif computer_action in defeats:
        result = f"{user_action} beats {computer_action}! You win!"
    else:
        result = f"{computer_action} beats {user_action}! You lose."
    return result


if __name__ == "__main__":
    while True:
        try:
            user_selection = get_user_selection(ACTIONS)
            print(user_selection)
            computer_selection = get_computer_selection(ACTIONS)
            print(computer_selection)
            determine_winner = get_determine_winner(
                VICTORIES, user_selection, computer_selection
            )
            print(determine_winner)
        except:
            range_str = f"[0, {len(ACTIONS) - 1}]"
            print(f"Invalid selection. Enter a value in range {range_str}")
            continue

        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            break
