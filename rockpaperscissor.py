# R > S, S > P, P > R
import random # impport module(files) : random

print("Welcome to the Rock, Paper and Scissor Game")

# Estimate the winner
def checkWinner(user, computer):
    if (user == computer):
        print(f"Computers:{computer} \nYour: {user}:\n============Tie==============")
        print('')
        return 'tie'

    elif(computer == "p" and user == 'r' or computer == 's' and user == 'p' or computer == "r" and user == "s"):
        print(f"Computers:{computer} \nYour: {user}:\n============You loose================")
        print('')
        return 'computer'
    else:
        print(f"Computers:{computer} \nYour: {user}:\n=============You won===============")
        print('')
        return 'user'

def game():
    options = ['r', 'p', 's', 'e']
    while True:
        print("==========choose from the menu===========")
        print('''
            p - Paper
            r - Rock
            s - Scissor
            e - back to main menu
        ''')
        user = input("Enter youse choice here: ")
        user = user.lower() # incase user inputs in uppercase   
        computer = random.choice(['r', 'p', 's'])
        
        if user not in options:
            print("Choose from the above options....")
            print("")
            continue
        elif(user == "e"):
            print("=========Thank you for playing the game===========")
            return 'exit'
        else:
            return checkWinner(user, computer)


# best of three
def bot():
    user_score = 0
    computer_score = 0
    tie = 0
    while user_score < 2 and computer_score < 2:
        result = game()
        if result == "computer":
            computer_score += 1
        elif result == "user":
            user_score += 1
        elif result == 'tie':
            tie += 1
        elif result == "exit":
            return
        print(f"Score => You: {user_score} | Computer: {computer_score} | Tie: {tie}")

    if user_score == 2:
        print('======You have won the game=======')

    elif computer_score == 2 :
        print('======Computer has won the game==========')

# infinite rounds
def inf():
    user_score = 0
    computer_score = 0
    total_rounds = 0
    tie = 0
    while True:
        result = game()
        total_rounds += 1
        if (result == 'exit'):
            break
        if result == "computer":
            computer_score += 1
        elif result == "user":
            user_score += 1
        elif result == 'tie':
            tie += 1
        print(f"Score => You: {user_score} | Computer: {computer_score} | Tie {tie} | Total Rounds: {total_rounds}")


def start():
    while True:
        print("==========choose the game mode===========")
        print('''
            1 - Best of three
            2 - Infinite rounds
            3 - Exit
        ''')
        main_menu = int(input("Enter your choice: "))
        if(main_menu == 1):
            bot()
        elif(main_menu == 2):
            inf()
        elif(main_menu == 3):
            print("=========Thank you for playing the game===========")
            break
        else:
            print('Invalid option')
start()