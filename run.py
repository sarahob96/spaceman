from pyfiglet import figlet_format
from words import space_words
import random

print(figlet_format("Welcome to Spaceman", font = "small"))

def game_intro():
    """ 
    Welcomes user and asks them for a username
    """
    print("Welcome to Spaceman, the word guessing game: Space edition")
    print("Please enter a username")

    user_name = input()
    print(f"Welcome {user_name}, time to play Spaceman!")


def random_word():
    """
    Selects a random word from the space_words array in the words.py file
    """
    word = random.choice(space_words)
   
    return word
 
def game():
    """
    
    """
    word = random_word()
    letters_guessed = []
    chances_remaining = 6
    letters = set(word)
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    

    while chances_remaining > 0:
        
        
        correct_word = ""

        for letter in word: 
                
            if letter in letters_guessed:
                     correct_word = correct_word + letter
            else:
                     correct_word = correct_word + "_ " 
                 
        print(correct_word)

        print(f"You have {chances_remaining} chances left")

        if len(letters_guessed) > 0:
         print(f"you have guessed these letters {letters_guessed}")

        enter_letter = input("Please enter a letter : ")
    

        if enter_letter in letters:
            print(f"You guessed a correct letter: '{enter_letter}' ")
        else:
             print(f" Sorry, '{enter_letter}' is not in the word")
             chances_remaining = chances_remaining - 1

        if enter_letter in letters_guessed:
             print(f"You have already guessed {enter_letter}")
        elif enter_letter in alphabet:
             letters_guessed.append(enter_letter)
               
        elif len(enter_letter) > 1:
            print("please enter one letter at a time")
        else: 
            print("please enter a valid letter")

        
     

game_intro()
random_word()
game()
