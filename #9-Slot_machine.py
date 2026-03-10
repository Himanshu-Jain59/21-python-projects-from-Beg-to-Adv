import random

options = {"🎱":5,
           "💯":10,
           "🍒":50,
           "🤑":100
           }
opt_list = ["🎱","💯","🍒","🤑"]
win_set = set()


print("Welcome!")
def get_deposit():
    while True:
        deposit = input("How much would u like to deposit? $")
        if deposit.isdigit():
            deposit = int(deposit)
            if deposit>0:
                break
            else:
                print("Enter amount more than 0.")
        else:
            print("Enter a number!")
    return deposit

def get_bets(balance,lines):
    while True:
        bet = input("How much would u like to bet on each line? $")
        if bet.isdigit():
            bet = int(bet)
            if bet>0:
                total_bet = bet*lines
                if total_bet<=balance:
                    break
                else:
                    print("Your balance is not enough make this bet. Try again!")
            else:
                print("Enter amount more than 0.")
        else:
            print("Enter a number!")
    return total_bet,bet

def get_lines():
    while True:
        lines = input("How many lines would u like to bet on(1-3)? ")
        if lines.isdigit():
            lines = int(lines)
            if 1<=lines<=3:
                break
            else:
                print("Choose between 1-3.")
        else:
            print("Enter a number!")
    return lines


def spin(total_bet,bet,lines,balance):
    winnings = 0
    for i in range(3):
        for j in range(3):
            print("|",end=" ")
            slot = random.choice(opt_list)
            print(slot,end=" ")
            win_set.add(slot)
            if lines==0:
                continue
            if j==2 and len(win_set)==1:
                win = win_set.pop()
                winnings += bet*options[win]
                lines-=1
        print("|")
        win_set.clear()
    print(f"You won ${winnings}")
    balance=balance-total_bet+winnings
    return balance


def main():
    balance = get_deposit()
    while True:
        if balance==0:
            break
        ans = input("Please enter to bet or Q to quit ")
        if ans.lower() == "q":
            break
        lines = get_lines()
        total_bet,bet = get_bets(balance,lines)
        print()
        balance=spin(total_bet,bet,lines,balance)
        print(f"Current Balance: ${balance}")
    print(f"You left with ${balance}")

main()