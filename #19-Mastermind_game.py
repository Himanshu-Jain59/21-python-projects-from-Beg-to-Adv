import random
COLORS=["R","W","B","G","Y","O"]
CODE_LEN=4
TRIES=10

def gen_code(colors , code_len):
    color_code=[]
    for _ in range(code_len):
        color = random.choice(colors)
        color_code.append(color)
    return color_code

def guess_code(colors,code_len):
    while True:
        guess = input("Enter a guess code (e.g. B R Y O): ").upper().split(" ")
        if len(guess)!=code_len:
            print(f"You must guess {code_len} colors")
            continue
        for color in guess:
            if color not in colors:
                print(f"Invalid color {color}. Try Again.")
                continue
        else:
            break
    return guess

def check(guess_code,real_code):
    color_count={}
    correct_pos=0
    incorrect_pos=0
    for color in real_code:
        if color not in color_count:
            color_count[color]=0
        color_count[color]+=1

    for guess , real in zip(guess_code,real_code):
        if guess == real:
            correct_pos+=1
            color_count[guess]-=1
        
    for guess in guess_code:
        if guess in color_count and color_count[guess]>0:
            incorrect_pos+=1
            color_count[guess]-=1
    return correct_pos,incorrect_pos

def game(colors,code_len,tries):
    print(f"Welcome to Mastermind, you have {tries} to guess the code.")
    print("The valid colors are ",*colors)

    color_code = gen_code(COLORS,CODE_LEN)
    for attempts in range(1,tries+1):
        print(f"Attempt {attempts}")
        guess=guess_code(COLORS,CODE_LEN)
        correct_pos ,incorrect_pos=check(guess,color_code)
        if correct_pos==code_len:
            print("Code Matched!")
            print(f"You guessed it in {attempts} attempts")
            break
        else:
            print(f"Correct position: {correct_pos} | Incorrect position: {incorrect_pos}")
    else:
        print("Game Over. The code was ",*color_code)

if __name__=="__main__":
    game(COLORS,CODE_LEN,TRIES)