from ast import While
import random

listOfAlphabet = ['a','b','c','d','e','f','g','h','i','j']
randomAlphabet = random.choice(listOfAlphabet)
numberOfGuesses = 0

name = input('What is your name? : ')
print(f'Hi {name}, I have guessed a alphabet from a to j')
print('Try to guess the Alphabet :')

while True:
    guess = input()
    numberOfGuesses += 1

    if guess != randomAlphabet:
        print("You guessed wrong. Guess another alphabet")
    else :
        print(f"{name}, you have guessed the right alphabet in {numberOfGuesses} tries.")
        break