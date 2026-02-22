print("Welcome to my Anime Quiz!")

playing = input("Enter player name: ")

print(f"Okay! {playing} Let's play :)")

anime_quiz = [
    {"q": "Who is the 'Copy Ninja' in Naruto?", "a": "Kakashi Hatake"},
    {"q": "What is Saitama's hero name?", "a": "One Punch Man"},
    {"q": "Who is the protagonist of 'Bleach'?", "a": "Ichigo Kurosaki"},
    {"q": "What is the name of Ash's first Pokémon?", "a": "Pikachu"},
    {"q": "Who is known as the 'Elric Brothers'?", "a": "Edward and Alphonse"},
    {"q": "What is the name of Luffy's crew?", "a": "Straw Hat Pirates"},
    {"q": "Which anime features 'Clow Cards'?", "a": "Cardcaptor Sakura"},
    {"q": "What is the name of the 'Death Note' shinigami?", "a": "Ryuk"},
    {"q": "In 'Demon Slayer', who is Tanjiro's sister?", "a": "Nezuko"},
    {"q": "What is Goku's birth name?", "a": "Kakarot"}
]

score=0

for i, item in enumerate(anime_quiz, 1):
    ans=input(f"{i}. {item["q"]} ")
    if(ans.lower() == item["a"].lower()):
        print("correct")
        score+=1
    else:
        print("incorrect")

print("score: "+str(score)+" out of "+str(len(anime_quiz)))