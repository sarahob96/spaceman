from pyfiglet import figlet_format
from words import space_words
import random



def game_intro():
    """ 
    Welcomes user and asks them for a username
    """

    print(figlet_format("Welcome to Spaceman", font = "small"))
    print("Welcome to Spaceman, the word guessing game: Space edition")
    menu()
    
    

def menu():
    print("\nMENU")
    print("1: Instructions")
    print("2: Play game \n")
    user_input = input("Please enter 1 or 2:  \n")
    if user_input == "1":
        instructions()
    elif user_input == "2":
            user_name()
    else:
        print("Please enter a valid option")

def instructions():
    print(" \nSPACEMAN")
    print("The aim of the game is to avoid the aliens by guessing the correct word before your chances run out ")
    print("1) You will have 6 chances to guess the right answer")
    print("2) All words are space related ")
    print("3) Each wrong guess means you are a step closer to the spaceship ")
    print("4) You will be given the chance to restart the game at the end of each game ")
    print("5) Goodluck \n")
    
    user_name()
    


def user_name():

    print("Please enter a username \n")

    global user_name
    user_name = input()
    print(f" \n Welcome {user_name}, time to play Spaceman!")
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
    word = random_word()
    letters_guessed = []
    chances_remaining = 6
    letters = set(word)
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    

    while chances_remaining > 0:
        
        print(illustrations(chances_remaining))
        correct_word = ""

        for letter in word: 
                
            if letter in letters_guessed:
                     correct_word = correct_word + letter
            else:
                     correct_word = correct_word + "_ " 
                 
        print(correct_word)
        

        print(f"You have {chances_remaining} chances left \n")

        if len(letters_guessed) > 0:
         print(f"you have guessed these letters {letters_guessed} \n")

        enter_letter = input("Please enter a letter : \n")
    

        

        if enter_letter in letters_guessed:
             print(f"You have already guessed {enter_letter}\n")
        elif enter_letter in alphabet:
             letters_guessed.append(enter_letter)  
             if enter_letter not in letters:
                 print(f" Sorry, '{enter_letter}' is not in the word")
                 chances_remaining = chances_remaining - 1
                 
        elif len(enter_letter) > 1:
            print("please enter one letter at a time\n")
        else:
            print("please enter a valid letter\n")
        

        if enter_letter in letters:
            print(f"You guessed a correct letter: '{enter_letter}'\n ")
            letters.remove(enter_letter)
        

        if len(letters) == 0:
            print("Congratulations, you have guessed the word")
            print("You escaped the aliens\n")
            exit()

    print(illustrations(chances_remaining))
    end_of_game()
    
        


def end_of_game():
        
        print("OH NO.. you have 0 chances left")
        print("You have been caught by the ALIENS \n")
        print("Would you like to restart the game?\n")
        answer = input("Please enter yes or no:  \n")
        if answer == "yes":
          game_intro()
        elif answer == "no":
          exit()
        else:
          print("Please enter a valid answer\n")

        
     

def exit():
    print(f"Thanks {user_name} for playing Spaceman \n")
    menu()

    

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
