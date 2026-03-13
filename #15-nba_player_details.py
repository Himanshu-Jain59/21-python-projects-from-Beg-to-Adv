from requests import get

BASE_URL = "https://api.server.nbaapi.com/api/playertotals"

def get_details(player):
    
    response = get(BASE_URL).json()["data"]
    
    for i in range(len(response)):
        if response[i]["playerName"] == player:
            print()
            print(f"Name: {response[i]["playerName"]}")
            print(f"Age: {response[i]["age"]}")
            print(f"Games: {response[i]["games"]}")
            print(f"Points: {response[i]["points"]}")
            print(f"Assists: {response[i]["assists"]}")
            print(f"Steals: {response[i]["steals"]}")
            print(f"Blocks: {response[i]["blocks"]}")
            print(f"Team: {response[i]["team"]}")
            print(f"Season: {response[i]["season"]}")

            break
    else:
        print("Not found ")
    

player = input("Enter player name: ")
get_details(player)