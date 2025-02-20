#Number Guessing Game:
#The computer generates a random number, and the user has to guess it 
# within a set range, receiving hints about whether their guess is too high or too low. 

import random



def number_guessing_game():
    print('Hello! Welcome to the Number Guessing Game')

    #Generate a random number 
    correct_number = random.randint(1,100)
    
    
    
    number_of_tries = 5
    print("I have chosen a number between 1 and 100. Can you guess what it is?")
    

    while number_of_tries > 0:
        
        #Added input validation. Prevents crashes if the user enters a non-numeric value.
        try:
            guessed_number = int(input(f"You have {number_of_tries} attempts left. Enter your guess:\n "))
        except ValueError:
            print("Oops! That’s not a valid number. Try again with a number between 1 and 100.")
            continue
        
        number_of_tries -= 1 #Deduct tries first
        
        if number_of_tries == 0:
            print('Oh bummer! You ran out of chances!') 
            return  
        
        if guessed_number < correct_number:
            print('You are very very close, just keep trying. Maybe a higher number. ')
        
        elif guessed_number > correct_number:
            print(f'Ahhh you\'ve gone too high! Lower down your numbers slightly! You have {number_of_tries} number of tries left!')
            
        else:
            print('Well done!! You guessed!')
            return  
       
number_guessing_game()

while True:
    play_again = input('\nWould you like to play again? (Y/N): ').strip().lower()
    
    if play_again == 'y':
        number_guessing_game() # Play the game again 
    print('Thanks for playing. Goodbye now!')
    break
          
        

    
    




