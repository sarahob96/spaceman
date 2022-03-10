from pyfiglet import figlet_format
from words import space_words

print(figlet_format("Welcome to Spaceman", font = "small"))

def game_intro():
    """ 
    Welcomes user and asks them for a username
    """
    print("Welcome to Spaceman, the word guessing game: Space edition")
    print("Please enter a username")

    user_name = input()
    print(f"Welcome {user_name}, time to play Spaceman!")


game_intro()