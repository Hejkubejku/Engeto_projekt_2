"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Jakub Heidlberk
email: jakub.heidlberk@seznam.cz
"""
from random import sample as s
from time import time as t

def four_code_gen ()-> int:
   print(f"Hi, there!\nI've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")
   first_digit = s("123456789", 1)[0]  
   other_digits = s([n for n in "0123456789" if n not in first_digit],3)
   return int(first_digit + "".join(other_digits))


def choose_number() -> int:
    while True:
        number = input("Enter 4-digit number, no repeats, no zero first: ")
        if not number.isdigit():
            print("Invalid input, please enter digits only.")
            continue
        if len(number) != 4 or len(set(number)) != 4 or number[0] == "0":
            print("Invalid format, try again.")
            continue
        return int(number)  


def compare_numbers (number: int, guess: int) -> tuple:
    bulls = 0
    cows = 0
    for i in range(4):
        if str(number)[i] == str(guess)[i]:
            bulls += 1
        elif str(guess)[i] in str(number):
            cows += 1
    return bulls, cows

def main() -> str:
    start = t()
    number = four_code_gen()
    attempts = 0
    while True:
        guess = choose_number()
        attempts += 1
        bulls, cows = compare_numbers(number, guess)
        print(f"{'Bull: ' if bulls == 1 else 'Bulls: '}{bulls}, {'Cow: ' if cows == 1 else 'Cows: '} {cows}")
        if bulls == 4:
            end = t()
            print(f"Congratulations! You've guessed the number {number} in {attempts} attempts and {int(end - start) // 60} mins and {int(end - start) % 60} seconds.")
            break
    return "Game over!"

main()
