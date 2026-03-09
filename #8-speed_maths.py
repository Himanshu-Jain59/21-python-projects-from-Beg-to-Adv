import random
import time

Operators = ["+","-","*"]
Min_operand = 3
Max_operand = 30
Total_Ques = 15

def genQues():
    left = random.randint(Min_operand,Max_operand)
    right = random.randint(Min_operand,Max_operand)
    operator = random.choice(Operators)

    expr = str(left)+" "+operator+" "+str(right)
    answer = eval(expr)

    return expr,answer

input("Press start to enter!")
print("--------------------")

start_time = time.time()

for i in range(Total_Ques):
    while True:
        expr,answer=genQues()
        guess = input(f"Q{i+1}. "+expr+" = ")
        if guess==str(answer):
            break

end_time = time.time()
total_time = round(end_time-start_time)

print("--------------------")
print("Nice work! You took "+str(total_time)+"sec")
