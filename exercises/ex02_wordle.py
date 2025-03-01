__author__ = "730737376"


# inital function that checks if the char parameter is in the str paraemter and if the char parameter is equal to 1
def contains_char(text: str, char: str) -> bool:
    """Checks if the given character is found within the text"""
    """Returns true if the the parameter char is found in the text"""

    assert len(char) == 1, f"len('{char}') is not 1"
    if len(char) != 1:
        return False

    index = 0
    found = False
    while index < len(text):
        if text[index] == char:
            found = True
        index += 1
    return found


# constant variables that make the green white and yellow boxes show up
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


# this implements the constant variables and returns a green white or yellow box with each guess
def emojified(guess: str, secret: str) -> str:
    """Returns a string of emoji representing the correctness of a guess compared to secret word using Wordle rules."""

    assert len(guess) == len(secret), "Guess must be same length as secret"

    result = ""
    index = 0
    while index < len(guess):
        if guess[index] == secret[index]:
            result += GREEN_BOX
        elif contains_char(secret, guess[index]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        index += 1
    return result


# input guess function that starts the user prompt and can only guess and expected length incorporated into it
def input_guess(expected_length: int) -> str:
    """Prompts the user for a guess of the expected length and ensures valid input."""

    guess = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


# main function puts it all together and has the user input implemented
def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""

    max_turns = 6
    turn = 1
    won = False

    while turn <= max_turns and not won:
        print(f"=== Turn {turn}/{max_turns} ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))

        if guess == secret:
            won = True
        else:
            turn += 1

    if won:
        print(f"You won in {turn}/{max_turns} turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
