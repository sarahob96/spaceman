"""
All imports are listed here
"""
import os
import sys
import random
from pyfiglet import figlet_format
from colorama import init, Fore
from words import space_words

init()


def reset_screen():
    """
    Resets the screen once called
    """
    os.system('reset')


def game_heading():
    """
    Displays the game banner
    """
    print(Fore.CYAN + figlet_format("Spaceman", font="small"))


def game_intro():
    """
    Welcomes user to the game
    """
    reset_screen()
    game_heading()
    print(Fore.YELLOW + "Welcome to Spaceman, the word guessing game")
    print(Fore.LIGHTCYAN_EX + "\nDo you think you can avoid the aliens?")
    print(Fore.LIGHTCYAN_EX + "Play now and find out..")
    print("----------------------------------------------")
    menu()


def menu():
    """
    Displays a menu to the user and asks for user input
    """
    print(Fore.WHITE + "\nMENU\n")
    print(Fore.LIGHTCYAN_EX + "1: Instructions")
    print(Fore.LIGHTCYAN_EX + "2: Play game \n")
    user_input = input(Fore.WHITE + "Please enter 1 or 2:  \n")
    if user_input == "1":
        instructions()
    elif user_input == "2":
        reset_screen()
        user_name()
    else:
        print("Please enter a valid option")
        reset_screen()


def instructions():
    "displays list of gameplay instructions"
    reset_screen()
    game_heading()
    print(Fore.YELLOW + " \nSPACEMAN \n")
    print(Fore.CYAN + "The aim of the game is to avoid an alien abduction")
    print("You can only do this by correctly guessing the word!\n")
    print(Fore.YELLOW + "1) You will have 6 chances to guess the right answer")
    print("2) All words are space themed")
    print("3) Each wrong guess means you are a step closer to the spaceship ")
    print("4) You can restart the game at the end of each game ")
    print("5) Goodluck \n")

    users_input = input(Fore.CYAN + "Press 1 to play the game:  ")
    if users_input == "1":
        reset_screen()
        user_name()


def user_name():
    """
    Asks user to enter a username and validates input
    """
    game_heading()
    print(Fore.WHITE + "Please enter a username \n")
    global users_name
    users_name = input().upper()
    while len(users_name) < 1:
        print(Fore.RED + "Please enter a valid username")
        print(Fore.WHITE + "Please enter a username \n")
        users_name = input().upper()

    print(
        Fore.LIGHTMAGENTA_EX +
        f" \nWelcome {users_name}, time to play Spaceman!")

    game()


def random_word():
    """
    Selects a random word from the space_words array in the words.py file
    """
    global word
    word = random.choice(space_words)

    return word


def game():
    """
    Contains the game workflow, runs a while loop until 0 chances
    remain or the correct word is guessed
    """

    word = random_word()
    letters_guessed = []
    chances_remaining = 6
    letters = set(word)
    alphabet = set('abcdefghijklmnopqrstuvwxyz')

    while chances_remaining > 0:

        print(Fore.WHITE + "\n=============================================\n")
        print(Fore.YELLOW + illustrations(chances_remaining))
        correct_word = Fore.YELLOW + ""

        for letter in word:

            if letter in letters_guessed:
                correct_word = correct_word + letter
            else:
                correct_word = correct_word + "_ "

        print(correct_word)

        print(
            Fore.LIGHTBLUE_EX +
            f"\nYou have {chances_remaining} chances left \n")

        if len(letters_guessed) > 0:
            print(
                Fore.LIGHTMAGENTA_EX +
                f"you have guessed these letters: {letters_guessed} \n")

        enter_letter = input(Fore.WHITE + "Please enter a letter : \n")

        if enter_letter in letters_guessed:
            print(Fore.RED + f"You have already guessed {enter_letter}\n")
        elif enter_letter in alphabet:
            letters_guessed.append(enter_letter)
            if enter_letter not in letters:
                print(
                    Fore.RED +
                    f"\nSorry, '{enter_letter}' is not in the word")
                chances_remaining = chances_remaining - 1

        elif len(enter_letter) > 1:
            print(Fore.RED + "please enter one letter at a time\n")
        else:
            print(Fore.RED + "please enter a valid letter\n")

        if enter_letter in letters:
            print(
                Fore.GREEN +
                f"You guessed a correct letter: '{enter_letter}'\n ")
            letters.remove(enter_letter)

        if len(letters) == 0:
            reset_screen()
            game_heading()
            print(f"Congratulations, you have guessed the word: {word}")
            print("You have escaped the aliens\n")
            thanks_for_playing()

    print(Fore.RED + "\n==============================================\n")
    print(illustrations(chances_remaining))
    end_of_game()


def end_of_game():

    """
    Gives user option to restart game when they have no chances
    """
    print(Fore.YELLOW + "OH NO.. you have 0 chances left")
    print("You have been caught by the ALIENS \n")
    print(Fore.LIGHTMAGENTA_EX + f"The correct word was: {word}\n ")
    print(Fore.WHITE + "Would you like to restart the game?\n")
    restart_answer = input("Please enter yes or no:  \n")

    if restart_answer == "yes":
        reset_screen()
        user_name()
    elif restart_answer == "no":
        reset_screen()
        game_heading()
        print(Fore.LIGHTMAGENTA_EX + f"Thanks for playing {users_name}\n")
        sys.exit()
    else:
        menu()


def thanks_for_playing():
    """
    Thanks user for playing and gives them choice to play again
    """
    print(Fore.MAGENTA + f"(Thanks for playing Spaceman {users_name}  \n")
    decision = input(Fore.WHITE + "\nWould you like another game? yes or no: ")
    if decision == "yes":
        reset_screen()
        user_name()
    elif decision == "no":
        reset_screen()
        print(Fore.YELLOW + "We hope to see you back playing Spaceman soon!")
        sys.exit()
    else:
        menu()


def illustrations(chances_remaining):

    """
    Contains all illustrations corresponding to amount of chances remaining
    """
    spaceman = [
        """
                      _________________
                    /      O  O  O      \\
                   (         _ _         )
                    \\_______|___|_______/
                     /\\               /\\
                             /|\\
                            / | \\
                           /  |  \\

                              0
                             \\|/
                             / \\

        """,
        """
                      _________________
                    /      O  O  O      \\
                   (         _ _         )
                    \\_______|___|_______/
                     /\\               /\\
                             /|\\
                            / | \\


                              0
                             /|\\
                             / \\

        """,
        """
                      _________________
                    /      O  O  O      \\
                   (         _ _         )
                    \\_______|___|_______/
                     /\\      /|\\      /\\


                              0
                             /|\\
                             / \\

        """,
        """
                      _________________
                    /      O  O  O      \\
                   (         _ _         )
                    \\_______|___|_______/
                     /\\               /\\


                              0
                             /|\\
                             / \\

    """,
        """
                      _________________
                    /      O  O  O      \\
                   (                     )
                    \\___________________/
                     /\\               /\\



                              0
                             /|\\
                             / \\

    """,
        """
                      _________________
                    /      O  O  O      \\
                   (                     )
                    \\___________________/





                              0
                             /|\\
                             / \\

    """,
        """

                              0
                             /|\\
                             / \\


    """,



    ]
    return spaceman[chances_remaining]


def spaceman_workflow():

    """
    Function that calls all functions used
    """

    game_intro()
    menu()
    instructions()
    user_name()
    random_word()
    game()
    end_of_game()
    thanks_for_playing()


spaceman_workflow()
