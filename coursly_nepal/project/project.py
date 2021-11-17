# random number game with humans
import random
x = int(input("Enter a number for range: "))
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    count = 0
    while guess != random_number:
        guess =  int(input(f"Guess the number between 1 to {x}: "))
        count += 1
        if count == 3:
            print("Sorry you have no more option, you lost!")
            break
        elif guess > random_number:
            print("Guess the lower number!!")
        elif guess < random_number:
            print("Guess the higher number!!")
        else:
            print("Yay, congratulation, u won the game.")
guess(x)

# playing random number game with computer
# a = int(input("Enter a number: "))
# def computer_guess(a):
#     low = 1
#     high = a
#     intake = ''
#     while intake != 'y':
#         if low != high:
#             intake = random.randint(low, high)
#         else:
#             intake = high # it can be low too
#         intake = input(f'the number {intake} is too high (H), too low (L), or correct (Y): ').lower()
#         if intake == 'l':
#             low += 1
#         elif intake == 'h':
#             high -= 1

#     print("Yay, congratulation, u won the game.")
# computer_guess(a)

# seisor paper rock
# import random
# tie = 0
# win = 0
# lose = 0
# while True:
#     print("""Enter you move: 
#     r - rock 
#     p - paper 
#     s - seisor 
#     q- quite """)
#     intake = input("Enter your option S, P, R or Q: ").lower()
#     computer = random.choice(['s', 'r', 'p'])
#     print(f'computer chose {computer}')
#     if intake == 'q':
#         print("Game Over!!!")
#         break
    
#     elif intake == computer:
#         print("we have same choice\n Game is Tie!")
#         tie += 1
#         print(f'your game is tie for {tie} times')

#     elif (intake == 'r' and computer == 's') or (intake == 's' and computer == 'p') or (intake == 'p' and computer == 'r'):
#         print('you win!')
#         win += 1
#         print(f'you have win the match for {win} times')

#     else:
#         print("you lost!")
#         lose += 1
#         print(f'you have lost the mathch for {lose} times')