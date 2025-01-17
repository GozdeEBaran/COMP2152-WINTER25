
#define the choices array
choices = ['rock', 'paper', 'scissors']

def main ():
    user_input=input("Enter your choice: rock, paper, or scissors: ").capatalize()

#validate user input
if user_input not in input
 raise ValueError("Invalid input. Please enter rock, paper, or scissors.")

 #convert the user input to an index
 player_choice = choices.index(user_input)
 
 #get the computer choice
 computer_choice = random.randint(0,2)
 print(f"Player chose {choices[player_choice]}")
 print(f"Computer chose {choices[computer_choice]}")   

#determine the winner

if player_choice == computer_choice:
    print("It's a tie!")
elif player_choice == 0 and computer_choice == 2 or \
    player_choice == 1 and computer_choice == 0 or \
    player_choice == 2 and computer_choice == 1:
    print("Player wins!") 
else:
    print("Computer wins!")
 
return True

#Run the game

