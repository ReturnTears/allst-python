import random
correct_number = random.randint(1, 10)
guessed_number = int(input("Guess a number between 1 and 10:"))
if guessed_number == correct_number:
    print("You guessed correctly!")
else:
    print("You guessed incorrectly!")


