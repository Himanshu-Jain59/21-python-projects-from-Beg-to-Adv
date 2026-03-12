import pygame
import time 

CLEAR = "\033[2J"
CLEAR_AND_RESET = "\033[H"
pygame.mixer.init()

def alarm(seconds):
    elapsedTime = 0
    print(CLEAR)
    while elapsedTime<seconds:
        time.sleep(1)
        elapsedTime+=1
        time_left = seconds-elapsedTime
        minutes_left = time_left//60
        seconds_left = time_left%60

        print(CLEAR_AND_RESET,f"The alarm will ring in {minutes_left:02d}:{seconds_left:02d}")
    pygame.mixer.music.load("alarm.mp3")  
    pygame.mixer.music.play()

    input("Alarm ringing! Press Enter to stop.")

minutes=int(input("Enter minutes: "))
seconds=int(input("Enter seconds: "))
total_sec = minutes*60+seconds

alarm(total_sec)