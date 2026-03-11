import turtle
import random
import time

WIDTH, HEIGHT = 600 , 500
COLORS = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black", "cyan"]

def get_racers():
    while True:
        racers = input("Enter no. racers (2-10): ")
        if racers.isdigit():    
            racers=int(racers)
            if racers>1:
                return racers
            else:
                print("Try again!")
        else:
            print("Try again!")

def set_screen():
    screen = turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title("Turtle Racing")

def create_turtles(colors):
    turtles = []
    spacing = WIDTH//(len(colors)+1)
    for i ,color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2+(i+1)*spacing,-HEIGHT//2+20)
        racer.pendown()
        turtles.append(racer)
    return turtles

def race(racers):
    while True:
        for racer in racers:
            distance = random.randrange(1,20)
            racer.forward(distance)
            x,y = racer.pos()
            if y>HEIGHT//2-10:
                return turtles.index(racer)



racers = get_racers()
random.shuffle(COLORS)
colors = COLORS[:racers]
set_screen()
turtles  = create_turtles(colors)
winner=race(turtles)
time.sleep(2)
print(f"The winner is {colors[winner]} turtle")
