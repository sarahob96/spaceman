from pyfiglet import figlet_format
from words import space_words
import random
import os
from colorama import init, Fore, Back, Style

init()


def reset_screen():
    os.system('reset')

def game_heading():
    print(Fore.CYAN + figlet_format("Spaceman", font = "small")) 

def game_intro():
    """ 
    Welcomes user
    """
    game_heading()
    print(Fore.YELLOW + "Welcome to Spaceman, the word guessing game: Space edition")

    
    menu()
    
    

def menu():

    
    
    print(Fore.WHITE +"\n     MENU    ")
    print("1: Instructions")
    print("2: Play game \n")
    user_input = input("Please enter 1 or 2:  \n")
    if user_input == "1":
        instructions()
        
    elif user_input == "2":
        reset_screen() 
        user_name()
            
    else:
        print("Please enter a valid option")
        reset_screen()

def instructions():
   
    reset_screen()
    game_heading()
    print(Fore.YELLOW + " \nSPACEMAN \n")
    print("The aim of the game is to avoid the aliens by guessing the correct word before your chances run out ")
    print("1) You will have 6 chances to guess the right answer")
    print("2) All words are space related ")
    print("3) Each wrong guess means you are a step closer to the spaceship ")
    print("4) You will be given the chance to restart the game at the end of each game ")
    print("5) Goodluck \n")
    
    users_input = input(Fore.CYAN + "Press 1 to play the game:  ")
    if users_input == "1":
        reset_screen()
        user_name()
    

def user_name():
    
    game_heading()
    print(Fore.WHITE + "Please enter a username \n")
    global users_name
    users_name = input().upper()

    print(Fore.LIGHTMAGENTA_EX + f" \nWelcome {users_name}, time to play Spaceman!")
    
    game()


def random_word():
    """
    Selects a random word from the space_words array in the words.py file
    """
    word = random.choice(space_words)
   
    return word
 
def game():
    """
    
    """
  
    global word 
    word = random_word()
    letters_guessed = []
    chances_remaining = 6
    letters = set(word)
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    

    while chances_remaining > 0:
        
        print(Fore.YELLOW + illustrations(chances_remaining))
        correct_word = ""

        for letter in word: 
                
            if letter in letters_guessed:
                     correct_word = correct_word + letter
            else:
                     correct_word = correct_word + "_ " 
                 
        print(correct_word)
        

        print(Fore.LIGHTBLUE_EX+ f"\nYou have {chances_remaining} chances left \n")

        if len(letters_guessed) > 0:
         print(Fore.LIGHTMAGENTA_EX + f"you have guessed these letters: {letters_guessed} \n")

        enter_letter = input(Fore.WHITE + "Please enter a letter : \n")
    

        

        if enter_letter in letters_guessed:
             print(Fore.RED + f"You have already guessed {enter_letter}\n")
        elif enter_letter in alphabet:
             letters_guessed.append(enter_letter)  
             if enter_letter not in letters:
                 print(Fore.RED + f"\nSorry, '{enter_letter}' is not in the word")
                 chances_remaining = chances_remaining - 1
                 
        elif len(enter_letter) > 1:
            print(Fore.RED + "please enter one letter at a time\n")
        else:
            print(Fore.RED + "please enter a valid letter\n")
        

        if enter_letter in letters:
            print(Fore.GREEN + f"You guessed a correct letter: '{enter_letter}'\n ")
            letters.remove(enter_letter)
        

        if len(letters) == 0:
            game_heading()
            print(f"Congratulations, you have guessed the word: {word}")
            print("You have escaped the aliens\n")
            exit()

    print(illustrations(chances_remaining))
    end_of_game()
    
        


def end_of_game():
        
        print(Fore.YELLOW + "OH NO.. you have 0 chances left")
        print("You have been caught by the ALIENS \n")
        print(Fore.LIGHTMAGENTA_EX+ f"The correct word was: {word}\n ")
        print(Fore.WHITE + "Would you like to restart the game?\n")
        answer = input("Please enter yes or no:  \n")
        if answer == "yes":
          reset_screen()
          user_name()
        elif answer == "no":
          reset_screen()
          game_heading()
          exit()
        else:
          print(Fore.RED + "Please enter a valid answer\n")

        
     

def exit():
    
    print(Fore.CYAN + f"Thanks {users_name} for playing Spaceman \n")
    exit_decision = input("\n Would you like another go at escaping the aliens? Enter yes or no: ")
    if exit_decision == "yes":
        reset_screen()
        user_name()
    elif answer == "no":
        reset_screen()
        print("We hope to see you back playing Spaceman soon!")
    

    

def illustrations(chances_remaining):
    spaceman = [
        """                  
                      _________________ 
                    /      O  O  O      \ 
                   (         _ _         )
                    \_______|___|_______/
                     /\               /\ 
                             /|\ 
                            / | \     
                           /  |  \ 

                              0   
                             \|/
                             / \  

        """,
    """                 
                      _________________ 
                    /      O  O  O      \ 
                   (         _ _         )
                    \_______|___|_______/
                     /\               /\ 
                             /|\ 
                            / | \     
                             
                      
                              0   
                             /|\ 
                             / \ 

    """,
    """             
                      _________________ 
                    /      O  O  O      \ 
                   (         _ _         )
                    \_______|___|_______/
                     /\      /|\      /\ 
                                       
                            
                              0   
                             /|\ 
                             / \ 
 
    """,
    """
                      _________________ 
                    /      O  O  O      \ 
                   (         _ _         )
                    \_______|___|_______/
                     /\               /\ 
                             

                              0   
                             /|\ 
                             / \ 

    """,
    """           
                      _________________ 
                    /      O  O  O      \ 
                   (                     )
                    \___________________/
                     /\               /\ 
                            
                       
                            
                              0   
                             /|\ 
                             / \ 

    """,
    """
                      _________________ 
                    /      O  O  O      \ 
                   (                     )
                    \___________________/
                                    
                            



                              0   
                             /|\ 
                             / \ 
 
    """,
    """ 
                    
                              0   
                             /|\ 
                             / \ 
    """,
    


    ]
    return spaceman[chances_remaining]
    

  

def functions ():
   
   
    game_intro()
    menu()
    instructions()
    user_name()
    random_word()
    game()
    end_of_game()
    exit()

functions()
