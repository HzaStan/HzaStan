"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Jan Staněk
email: rubadub@seznam.cz
"""

import random
import time

def generate_secret_number():
    """Vygeneruje tajenku"""
    while True:
        number = str(random.randint(1000, 9999))  # Číslo mezi 1000 a 9999
        if number[0] != '0':  # Ověří, že nezačíná nulou
            return number
        print(number)

def get_valid_input():
    """Získá validní 4místný vstup od uživatele."""
    while True:
        user_input = input("Enter a 4-digit number: ")

        # Zkontroluj, zda je délka vstupu 4
        if len(user_input) != 4:
            print("Error: your number must have 4 digits!")
            print("-----------------------------------------------")
            continue
        
        # Zkontroluj, zda vstup obsahuje pouze čísla
        if not user_input.isdigit():
            print("Error: your input must be a number!")
            print("-----------------------------------------------")
            continue
        
        # Zkontroluj, zda nezačíná nulou
        if user_input.startswith("0"):
            print("Error: the number cannot begin with a zero!")
            print("-----------------------------------------------")
            continue

        # Pokud je vstup validní, vrať ho
        return user_input

def evaluate_guess(secret, guess):
    """Vyhodnotí bulls a cows správně."""
    bulls = 0
    cows = 0
    secret_used = [False] * 4  # Pro kontrolu, které číslice tajenky byly použity jako bulls
    guess_used = [False] * 4   # Pro kontrolu, které číslice uživatelského vstupu byly použity

    # První průchod: najdi bulls
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
            secret_used[i] = True  # Označ číslici jako použitou pro bull
            guess_used[i] = True

    # Druhý průchod: najdi cows
    for i in range(4):
        if not guess_used[i]:  # Pokud číslice není bull
            for j in range(4):
                if not secret_used[j] and guess[i] == secret[j]:
                    cows += 1
                    secret_used[j] = True  # Označ číslici tajenky jako použitou pro cow
                    break

    return bulls, cows

# Hlavní program
tajenka = generate_secret_number()
print("Hi there! I have generated a random 4-digit number.")
print("Let's play Bulls-n-Cows game with me!")
# print(tajenka)
guesses = 0 
total_time = 0

while True:
    guesses += 1   # Počítadlo pokusů
    input_starttime = time.time()  # Začátek měření času pro vstup
    user_guess = get_valid_input()  # Získání validního vstupu
    input_endtime = time.time()    # Konec měření času pro vstup
    total_time += input_endtime - input_starttime  # Přičtení času pro tento pokus
    bulls, cows = evaluate_guess(tajenka, user_guess)  # Vyhodnocení vstupu
    
    print(f"{bulls} bull{'s' if bulls != 1 else ''}, {cows} cow{'s' if cows != 1 else ''}")
    print("-----------------------------------------------")

    if bulls == 4:
        print(f"Congrats you've got it in {guesses} guesses!")
        print(f"It took you {total_time:.0f} seconds only to get it right.")
        break



