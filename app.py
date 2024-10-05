import random

class Game(object):

    def __init__(self):
        self.difficulty_levels = {
            "Easy": 10,
            "Medium": 5,
            "Hard": 3
        }
        self.difficulty_level = None
        self.number = random.randint(1, 100)
        self.guessed_numbers = []
        self.current_attempt = 0
        self.max_attempts = 0

    def get_difficulty_level(self):
        for level in self.difficulty_levels:
            print(f"{level} - Attempts: {self.difficulty_levels[level]}")
        print("")
        while True:
            difficulty_level = input(f"Choose difficulty level ({', '.join(self.difficulty_levels.keys())}): ")
            if difficulty_level in self.difficulty_levels:
                self.max_attempts = self.difficulty_levels[difficulty_level]
                print(f"Great! You have chosen the {difficulty_level} difficulty level.")
                return difficulty_level
            else:
                print("Invalid difficulty level. Please try again.")

    def get_guessed_number(self):
        while True:
            try:
                guessed_number = int(input(f"Attempt {self.current_attempt + 1}/{self.max_attempts}. Enter your guess: "))
                if guessed_number < 1 or guessed_number > 100:
                    print("Invalid number. Please enter a number between 1 and 100.")
                elif guessed_number in self.guessed_numbers:
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
        self.difficulty_level = self.get_difficulty_level()
        print("""
Let's start the game!
""")

        while self.current_attempt < self.max_attempts:
            guessed_number = self.get_guessed_number()
            self.guessed_numbers.append(guessed_number)
            self.current_attempt += 1
            if guessed_number == self.number:
                print(f"Congratulations! It was {self.number}! You guessed the correct number in {self.current_attempt} attempts.")
                break
            else:
                relative = "greater" if guessed_number < self.number else "less"
                print(f"Incorrect! The number is {relative} than {guessed_number}.")
        if guessed_number != self.number:
            print(f"Game Over! The number was {self.number}.")

if __name__=="__main__":
    g = Game()
    g.play()