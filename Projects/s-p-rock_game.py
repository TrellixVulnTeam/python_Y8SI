import random
# from typing import Counter 

print('\nWelcome to the real gaming world !')
chose = ["secissor", "paper" "rock"]
computer_win = 0
user_win = 0
tie_game = 0

condition  = True
while True:
    comp_value = random.choice(chose).lower()
    user_value = input('Enter you option(scissor(s), paper(p), rokc(r) and q to quite the game): ').lower()

    if user_value == comp_value:
        print('game is tie!')
        tie_game += 1
        print(f'Game tie for {tie_game} time')

    elif user_value == 'secisor' or user_value == 's':
        if comp_value == 'paper' or comp_value == 'p':
            print("user wins the game!")
            user_win += 1
            print(f'you have won the game for {user_win} times') 
        else:
            print('computer win the game!')
            computer_win += 1
            print(f'you have lost the game for {computer_win} times') 
            
    elif user_value == 'paper' or user_value == 'p':
        if comp_value == 'rock' or comp_value == 'r':
            print("user wins the game!") 
            user_win += 1
            print(f'you have won the game for {user_win} times') 
        else:
            print('computer wins the game!') 
            computer_win += 1
            print(f'you have lost the game for {computer_win} times') 

    elif user_value == 'rock' or user_value == 'r':
        if comp_value == 'secissor' or comp_value == 's':
            print(f'user win the game!')
            user_value += 1
            print(f'you have won the game for {user_win} times') 
        else:
            print(f'computer win the game!')
            computer_win += 1
            print(f'you have lost the game for {computer_win} times') 

    elif user_value == 'q' or user_value == 'Q':
        break
    else:
        print('Wrong commangd!')



# import random
# game_list = ['rock', 'paper', 'scissor']
# computer = c = 0
# command = p = 0
# print("score: computer" + str(c) + 'player' + str(p))
# # the loop 
# run = True
# while run:
#     computer_choose = random.choice(game_list)
#     command = input("rock, paper, scissors or quite: ")
#     if command == computer_choose:
#         print("tie!")
#     elif command == 'rock':
#         if computer_choose == 'scissor':
#             print("players won!")
#             p += 1
#         else:
#             print("computer won!")
#             c += 1

#     elif command == 'paper':
#         if computer_choose == "rock":
#             print("player won!")
#             p =+1
#         else:
#             print("computer won!")
#             c =+1


#     elif command == 'scissors':
#         if computer_choose == "paper":
#             print('you won!')
#             p =+1
#         else:
#             print("computer won!")
#             c += 1

#     elif command == "Quit":
#         break
#     else:
#         print("wrong command! ")
    
    # print("player: "+ command)
    # print("computer: "+ computer_choose)
    # print("")
    # print("score: computer "+ str(c))
    # print("player "+ str(p))
    # print("")