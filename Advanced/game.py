import random

COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    return [random.choice(COLORS) for _ in range(CODE_LENGTH)]

def guess_code():
    while True:
        guess = input("Guess: ").upper().split(" ")

        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors.")
            continue

        if all(color in COLORS for color in guess):
            return guess
        else:
            print(f"Invalid colors in your guess. Try again. Valid colors: {', '.join(COLORS)}")

def check_code(guess, real_code):
    color_counts = {color: real_code.count(color) for color in COLORS}
    correct_pos = 0
    incorrect_pos = 0

    # First pass: check for correct positions
    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_counts[guess_color] -= 1

    # Second pass: check for correct colors in wrong positions
    for guess_color, real_color in zip(guess, real_code):
        if guess_color != real_color and color_counts.get(guess_color, 0) > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos

def game():
    print(f"Welcome to Mastermind! You have {TRIES} tries to guess the code.")
    print("The valid colors are:", ', '.join(COLORS))

    code = generate_code()
    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print(f"You guessed the code in {attempts} tries!")
            break

        print(f"Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos}")

    else:
        print("You ran out of tries. The code was:", ' '.join(code))

if __name__ == "__main__":
    game()
