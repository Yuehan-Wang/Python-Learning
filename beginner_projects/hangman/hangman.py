import random
from words import words
import string


def get_valid(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid(words)
    word_letters = set(word)
    alph = set(string.ascii_uppercase)
    used_letters = set()

    while len(word_letters) > 0:
        print('your guess ',' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('word:','  '.join(word_list))
        user_letter = input("type a letter:").upper()
        if user_letter in alph - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)  
                print('')
        elif user_letter in used_letters:
            print("you have already guessed it")
        else: 
            print("invalid")
    print('YAYYY')



hangman()

