import random

options = ["rock","paper","scissors"]
user_win = 0
comp_win = 0

while (True):
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if (user_input=="q"):
        break
    if user_input not in options:
        continue
    r=random.randint(0,2)
    comp_pick = options[r]
    if (user_input=="rock" and comp_pick=="scissors"):
        print("Computer picked",comp_pick)
        print("You won!")
        user_win +=1
    elif (user_input=="scissors" and comp_pick=="paper"):
        print("Computer picked",comp_pick)
        print("You won!")
        user_win +=1
    elif (user_input=="paper" and comp_pick=="rock"):
        print("Computer picked",comp_pick)
        print("You won!")
        user_win +=1
    elif (user_input==comp_pick):
        print("Computer picked",comp_pick)
        print("Match Draw!")
    else:
        comp_win+=1
        print("Computer picked",comp_pick)
        print("You lost!")

print("Scoreboard")
print("User:",user_win,end="   ")
print("Computer:",comp_win)

print("Goodbye!")
    