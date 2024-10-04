import random

class Game(object):

    def __init__(self):
        self._difficulty_levels = {
            "Easy": 10,
            "Medium": 5,
            "Hard": 3
        }
        self._difficulty_level = None
        self._number = None
        self._guessed_numbers = []
        self._current_attempt = 0
        self._max_attempts = 0

    def _get_difficulty_level(self):
        for level in self._difficulty_levels:
            print(f"{level} - Attempts: {self._difficulty_levels[level]}")
        while True:
            difficulty_level = input("Choose difficulty level (Easy, Medium, Hard): ")
            if difficulty_level in self._difficulty_levels:
                self._max_attempts = self._difficulty_levels[difficulty_level]
                print(f"Great! You have chosen the {difficulty_level} difficulty level.")
                return difficulty_level
            else:
                print("Invalid difficulty level. Please try again.")

    def _get_guessed_number(self):
        while True:
            try:
                guessed_number = int(input(f"Attempt {self._current_attempt + 1}/{self._max_attempts}. Enter your guess: "))
                if guessed_number < 1 or guessed_number > 100:
                    print("Invalid number. Please enter a number between 1 and 100.")
                elif guessed_number in self._guessed_numbers:
                    print("You have already guessed this number. Try again.")
                else:
                    return guessed_number
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def play(self):
        print("""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have a limited number of attempts to guess the number.
Good luck!
""")
        self._number = random.randint(1, 100)
        self._difficulty_level = self._get_difficulty_level()
        print("")
        print("Let's start the game!")
        print("")

        while self._current_attempt < self._max_attempts:
            guessed_number = self._get_guessed_number()
            self._guessed_numbers.append(guessed_number)
            self._current_attempt += 1
            if guessed_number == self._number:
                print(f"Congratulations! You guessed the correct number in {self._current_attempt} attempts.")
                break
            else:
                relative = "greater" if guessed_number < self._number else "less"
                print(f"Incorrect! The number is {relative} than {guessed_number}.")
        if guessed_number != self._number:
            print(f"Game Over! The number was {self._number}.")

if __name__=="__main__":
    g = Game()
    g.play()