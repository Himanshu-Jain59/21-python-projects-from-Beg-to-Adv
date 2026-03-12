import curses
from curses import wrapper
import time
import queue

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

def print_maze(maze,stdsrc,path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i , row in enumerate(maze):
        for j,col in enumerate(row):
            if (i,j) in path:
                stdsrc.addstr(i,j*2,"X",RED)
            else:
                stdsrc.addstr(i,j*2,col,BLUE)

def find_start(maze,start):
    for i , row in enumerate(maze):
        for j,col in enumerate(row):
           if col == start:
               return i,j
    return None

def find_path(maze,stdsrc):
    start = "O"
    end="X"
    start_pos = find_start(maze,start)
    q  = queue.Queue()
    q.put((start_pos,[start_pos]))
    visited = set()

    while not q.empty():
        current_pos , path = q.get()
        row , col = current_pos
        stdsrc.clear()
        print_maze(maze,stdsrc,path)
        time.sleep(0.2)
        stdsrc.refresh()
        
        if maze[row][col]==end:
            return path
        neighbours=find_neighbour(maze,row,col)
        for neighbour in neighbours:
            if neighbour in visited:
                continue
            r,c = neighbour
            if maze[r][c]=="#":
                continue
            next_pos = path + [neighbour]
            q.put((neighbour,next_pos))
            visited.add(neighbour)
        
def find_neighbour(maze,row,col):
    neighbour=[]
    if row>0: #UP
        neighbour.append((row-1,col))
    if row+1<len(maze):#down
        neighbour.append((row+1,col))
    if col>0:#left
        neighbour.append((row,col-1))
    if col+1<len(maze[0]):#right
        neighbour.append((row,col+1))

    return neighbour


def main (stdsrc):
    curses.init_pair(1,curses.COLOR_BLUE,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    
    find_path(maze,stdsrc)
    stdsrc.getch()
wrapper(main)