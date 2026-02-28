import random

def roll():
    value = random.randint(1,6)
    return value

while True:
    players=input("Enter the number of players (2-4): ")
    if (players.isdigit()):
        players = int(players)
        if (2<=players<=4):
            break
        else:
            print("must be between 2-4")
    else:
        print("invalid input try again")

players_number =[0 for _ in range(players)]
max_num = 25

while (max(players_number)<max_num):
    for idx in range(len(players_number)):
        if not (max(players_number)<max_num):
            break
        print("\nPlayer",idx+1,"turn")
        print("current score:",players_number[idx])
        # currScore = 0
        while True:
            if not (max(players_number)<max_num):
                break
            choice = input("Would u like to roll (y/n): ")
            if not (choice.lower()=="y"):
                break
            value = roll()
            if (value==1):
                print("you just rolled 1")
                players_number[idx]=0
                break
            else:
                print("you just rolled",value)
                # currScore+=value
                players_number[idx]+=value
                print("score:",players_number[idx])
        
        print("you current totoal is",players_number[idx])

max_score = max(players_number)
winner =players_number.index(max_score)
print("\nwinner is player",winner+1)
print("score:",max_score)
