from ast import While
import random

randomNumber = random.randint(1, 10)
numberOfGuesses = 0

name = input('What is your name? : ')
print(f'Hi {name}, I have guessed a number from 1 to 10')
print('Try to guess the number :')

while True:
    guess = int(input())
    numberOfGuesses += 1

    if guess > randomNumber:
        print("Your guess is too high!!")
    elif guess < randomNumber:
        print("Your guess is too low!!")
    else :
        print(f"{name}, you have guessed the right number in {numberOfGuesses} tries.")
        break