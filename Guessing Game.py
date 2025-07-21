import random

def number_guessing_game():
    guess_count = 0
    random_number = random.randint(1, 100)

    print("Welcome to MY Number Guessing Game!")
    print("There are number 1-100, Let's try hehehehehe!")

    while True:
        try:
            guess = int(input("Let's guess a number between 1-100. Which one would you like?: "))

            guess_count += 1

            if guess > random_number:
                print("Too high! Again try again!")
            elif guess < random_number:
                print("I said Too Low!")
            else:
                print("Correct! FINALLY!")
                break

        except ValueError:
            print("Number! Try again!. Guessing Number Game, Need to put NUmber!")

if __name__ == "__main__":
    number_guessing_game()
