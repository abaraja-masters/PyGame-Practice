# Game: This is a Guess the Number game via console.
# Author: Anthony Baraja
import random
from os import system, name

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

numOfGuesses = 6

clear()
# Prompt user's name
print('Hello! What is your name?')
myName = input()
clear()

number = random.randint(1, 20)
print(f'Well, {myName}, I am thinking of a number between 1 and 20.')

for guessesTaken in range(numOfGuesses):
    print(f'\nYou have {numOfGuesses - guessesTaken} guesses remaining.')
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Your guess is too low.')
    
    if guess > number:
        print('Your guess is too high.')
    
    if guess == number:
        print()
        break

clear()

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print(f'Good job, {myName}! You guessed my number in {guessesTaken} guesses!')

if guess != number:
    number = str(number)
    print(f'Nope. The number I was thinking of was {number}.')