import random

answer = random.randint(0, 100)


def guess_game(guess):
    poi = 0  # variable used for times guessed

    while guess != answer:  # automatically stopped after guessing correctly
        guess = int(input("Enter a numer: "))
        try:
            a = int(input("Hay nhap so: "))
        except ValueError:
            a = int(input("Hay nhap so: "))
        if guess > 100 or guess < 0:  # put limit to input from user
            print("Please enter a number from 0 to 100")
        else:
            if guess < answer:
                print("Too small")
            elif guess > answer:
                print("Too big")
            elif guess == answer:
                print("Correct")

        poi += 1
        print(f"You have guessed {poi} times.")


guess_game(1)
