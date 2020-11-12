import random
import re
import sys
import string
#from words import word_list
from display_hangman import stages
from display_hangman_hard import stages_hard

def Main():
    f=open("countries_capitals.txt", "r")
    word_list=f.read().replace('\n'," | ").split(" | ")
    #word_list = open("countries_capitals.txt", "r")
    f.close()
    word=random.choice(word_list).lower()
    player_name=input('You can close the game anytime - just write "quit". \nHello player, What is your name?\n')
    if player_name == "quit":
        print('Goodbye')
        sys.exit(0)
    player_answer=input(f"Hello {player_name} Do you wanna play in hangman?\n").lower()
    if player_answer == "quit":
        print('Goodbye')
        sys.exit(0)
    while player_answer != 'yes' and player_answer != 'no':
        player_answer=input(f"Answer: 'yes' or 'no'. {player_name}, do you wanna play in hangman?\n").lower()
    if player_answer == 'yes':
        levels=input("Let's play. Enter your level: (h)ard or (e)asy?\n")
        if levels == "quit":
            print('Goodbye')
            sys.exit(0)
        while levels != 'h' and levels != 'e':
            levels=input('Enter your level: (h)ard or (e)asy\n')
        if levels == 'h':
            lives = 4
            while len(word)<(5):
                word=random.choice(word_list).lower()
            Play(word, lives)
        else:
            lives=6
            while len(word)>=(5):
                word=random.choice(word_list).lower()
            Play(word, lives)
    elif player_answer == "quit":
        print('Goodbye')
        sys.exit(0)
    else:
        print('Goodbye')


def Play(word,lives):
    i=0
    word_guessing_ = []
    word_list=list(word)
    word_length=[]
    for i in word:
        if i.isalpha():
            word_length.append(i)
            i='_'
            word_guessing_.append(i)
        else:
            word_guessing_.append(i)
    word_guessing =''.join(word_guessing_)
    print(f"The word is {len(word_length)} letters length")
    print(word_guessing)
    stages_iterator=iter(stages)
    stages_hard_iterator=iter(stages_hard)
    guess=False
    guessed_letters=[]
    if lives == 4:
        while lives>0 and guess == False:
            char=input('Guess the letter:\n')
            if char == "quit":
                print('Goodbye')
                sys.exit(0)
            if len(char)==1 and char.isalpha():
                if char in guessed_letters:
                    print('You have already guessed this letter ' + char)
                elif char not in word:
                    print(char, "is not in the word.")
                    lives -= 1
                    guessed_letters.append(char)
                    print(f"You have {lives} lives")
                    print(next(stages_hard_iterator))
                    _stage=(stages_hard_iterator)
                    word_guessing=string.capwords(word_guessing, sep=None)
                    print(word_guessing)
                else:
                    print(f"Good job {char} is in the word!")
                    guessed_letters.append(char)
                    word_as_list = list(word_guessing)
                    indices = [i for i, letter in enumerate(word) if letter == char]
                    for index in indices:
                        word_as_list[index] = char
                    word_guessing = "".join(word_as_list)
                    word_guessing=string.capwords(word_guessing, sep=None)
                    print(word_guessing)
                    if "_" not in word_guessing:
                        print('Great! You guessed the word!')
                        guess = True
            elif len(char.lower()) == len(word.lower()):
            #and char.isalpha():
                if char.lower() == word.lower():
                    word=string.capwords(word, sep=None)
                    print(f'Great! You guessed the word {word}!')
                    guess=True
                else:
                    print('No, You have not guessed the word.')
                    lives-=1
                    print(f"You have {lives} lives")
                    print(next(stages_hard_iterator))    
                    _stage=(stages_hard_iterator)
                    word_guessing=string.capwords(word_guessing, sep=None)
                    print(word_guessing)  
            elif len(char.lower()) !=  len(word.lower()):
                print(f"The word must be {len(word)} letters.")      
        if lives==0:
            word_guessing=string.capwords(word_guessing, sep=None)
            print(f'You lose. The word was {word}')

    elif lives == 6:
        while lives>0 and guess == False:
            char=input('Guess the letter:\n').lower()
            if char == "quit":
                print('Goodbye')
                sys.exit(0)
            if len(char)==1:
            #and char.isalpha():
                if char in guessed_letters:
                    print('You have already guessed this letter ' + char)
                elif char not in word:
                    print(char, "is not in the word.")
                    lives -= 1
                    guessed_letters.append(char)
                    print(f"You have {lives} lives")
                    print(next(stages_iterator))
                    _stage=(stages_hard_iterator)
                    word_guessing=string.capwords(word_guessing, sep=None)
                    print(word_guessing)
                else:
                    print(f"Good job {char} is in the word!")
                    guessed_letters.append(char)
                    word_as_list = list(word_guessing)
                    indices = [i for i, letter in enumerate(word) if letter == char]
                    for index in indices:
                        word_as_list[index] = char
                    word_guessing = "".join(word_as_list)
                    word_guessing=string.capwords(word_guessing, sep=None)
                    print(word_guessing)
                    if "_" not in word_guessing:
                        print('Great! You guessed the word!')
                        guess = True
            elif len(char.lower()) == len(word.lower()):
            #char.isalpha():
                if char.lower() == word.lower():
                    word=string.capwords(word, sep=None)
                    print(f'Great! You guessed the word {word}!')
                    guess=True
                else:
                    print('No, You have not guessed the word.')
                    lives-=1
                    print(next(stages_iterator))
                    _stage=(stages_hard_iterator)
                    word_guessing=string.capwords(word_guessing, sep=None)
                    print(word_guessing)
            elif len(char.lower()) !=  len(word.lower()):
                print(f"The word must be {len(word)} letters.")
             
        if lives==0:
            word=string.capwords(word, sep=None)
            print(f'You lose. The word was {word}')
            
Main()
