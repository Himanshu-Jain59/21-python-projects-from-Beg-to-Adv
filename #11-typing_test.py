import time
import random
import curses
from curses import wrapper

def load_text():
    with open("text.txt","r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()

def start_screen(stdsrc):
    stdsrc.clear()
    stdsrc.addstr("Welcome to Typing Test")
    stdsrc.addstr("\nPress enter to start")
    stdsrc.refresh()
    stdsrc.getkey()

def display_text(stdsrc, target,current,wpm=0):
    stdsrc.addstr(target)
    stdsrc.addstr(1,0,f"WPM: {wpm}")
    for i,char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if char!=correct_char:
            color=curses.color_pair(2)
        stdsrc.addstr(0,i,char,color)
    

def wpm_test(stdsrc):
    target_text = load_text()
    entered_text=[]
    wpm = 0
    start_time = time.time()
    stdsrc.nodelay(True)

    while True:
        stdsrc.clear()
        elapsed_time=max(time.time()-start_time,1)
        wpm = round((len(entered_text)/(elapsed_time/60))/5)

        display_text(stdsrc,target_text,entered_text,wpm)
        stdsrc.refresh()
        if "".join(entered_text)==target_text:
            stdsrc.nodelay(False)
            break
        try:
            key = stdsrc.getkey()
        except:
            continue
        if ord(key )==27:
            break
        if key in ("KEY_BACKSPACE","\b","\x7f"):
            if len(entered_text)>0:
                entered_text.pop()
        elif len(entered_text)<len(target_text):
            entered_text.append(key)


def main(stdsrc):
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_WHITE,curses.COLOR_BLACK)

    start_screen(stdsrc)
    while True:
        wpm_test(stdsrc)
        stdsrc.addstr(2,0,"You completed the test. Press enter to continue....")
        key = stdsrc.getkey()
        if ord(key) == 27:
            break


wrapper(main)