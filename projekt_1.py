"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jan Staněk
email: rubadub@seznam.cz
"""
import sys

texts = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

registered_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# Funkce přihlášení
def login():
    username = input("Your username: ")
    if username in registered_users:
        password = input("Password: ")
        
        # Ověříme, zda heslo odpovídá
        if registered_users[username] == password:
            print(f"Welcome to the app, {username}! We have {len(texts)} texts to be analyzed.")
            return True
        else:
            print("Incorrect password. Terminating the program...")
            sys.exit()
    else:
        print("Unregistered user. Terminating the program...")
        sys.exit()
        
# Uživatel je přihlášen, pokračujeme v aplikaci výběrem textu
if login():
    while True:
        selected_text = input(f"Enter a number between 1 and {len(texts)} to select: ")
        if selected_text.isdigit():  
            number = int(selected_text) 
        if 1 <= number <= len(texts):  
            print(f"You selected text number {number}. Analyzing...")
            break  # Pokud je výběr validní, opustíme cyklus a pokračujeme
        else:
            print("Incorrect input")

# Hlavní program: počty slov
analyze_text = texts[number - 1]
words = analyze_text.split()
total = len(words)
titlecase = 0
uppercase = 0
lowercase = 0
digit = 0
sum = 0

for word in words:
    if word[0].isupper():
        titlecase += 1
    if word.isupper() and not any(char.isdigit() for char in word):
        uppercase += 1
    if word.islower():
        lowercase += 1 
    if word.isdigit():
        digit += 1
        sum += int(word)

print("There are", total, "words in the selected text.")
print("There are", titlecase, "titlecase words.")
print("There are", uppercase, "uppercase words.")
print("There are", lowercase, "lowercase words.")
print("There are", digit, "numeric strings.")
print(f"The sum of all the numbers is {sum}.")

#Hlavní program: frekvence výskytu slove dle jejich délky
word_length_count = {}

for word in words:
    clean_word = word.strip(",.?!")
    length = len(clean_word)
    if length > 0:  
        if length in word_length_count:
            word_length_count[length] += 1
        else:
            word_length_count[length] = 1

max_stars_length = max(len('*' * count) for count in word_length_count.values())
print("-" * 40)
print("LEN|".ljust(3), "OCCURRENCES", "|NR.".rjust(max_stars_length - 6))
print("-" * 40)
for length in sorted(word_length_count):
    stars = '*' * word_length_count[length]
    print(f"{length:>3}|{stars:<{max_stars_length}}   |{word_length_count[length]}")