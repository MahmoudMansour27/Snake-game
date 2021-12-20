import random #lib used for some ramdom purpose
import  curses #lib used for screen purpose
#export TERM = linux
#export TERMINFO = /etc/terminfo
import os
os.environ['PWNLIB_NOTERM'] = '1'
os.environ['TERM'] = 'linux'
#the last few lines used to set enviroment variables TERM and TERMINFO.
#from pwn import *  # the modifications need to happen before this import

screen = curses.initscr() #intialize scren
curses.curs_set(0) #visiablity of cursor
screen_hight, screen_width = screen.getmaxyx() #getmaxyx function used to get screen width and height
windon = curses.newwin(screen_hight,screen_width, 0,0) #creating a window
windon.keypad(1)
windon.timeout(100) #refresh the window
snk_x = screen_width//4 #intial x-axis position
snk_y = screen_hight//2 #intial y-axis position
snake =[
    [snk_y, snk_x],
    [snk_y-1, snk_x],
    [snk_y-2, snk_x]
]
# intial snake body with three blocks
food = [screen_hight//2, screen_width//2] #intial food position
windon.addch(food[0], food[1], "O") #use add charcter function to add food charcter which is "O" in intial food position
key = curses.KEY_RIGHT #initiaztion key var with right diriction
while True:  #infinte loop to see the next key and add food in random lib
    nextKey = windon.getch()  #get key value from keyboard
    key = key if nextKey == -1 else nextKey
    if snake[0][0] in [0, screen_width] or  snake[0][0] in [0, screen_hight] or snake[0][0] in [screen_hight, screen_width] or snake[0] in snake[1:]: #chech if snake hit any thing
        curses.endwin()
        quit()
    #get the next key and change x and y position
    newPosition = [snake[0][0], snake[0][1]]
    if key == curses.KEY_RIGHT:
        newPosition[1] += 1
    elif key == curses.KEY_LEFT:
        newPosition[1] += -1
    elif key == curses.KEY_UP:
        newPosition[0] -= 1
    elif key == curses.KEY_DOWN:
        newPosition[0] += 1

    snake.insert(0, newPosition)
    #create new random food
    if snake[0] == food:
        food = None
        while (food == None):
            newFood = [random.randint(1, screen_hight-1), random.randint(1, screen_width-1)]
            food = newFood if newFood not in snake else None
        windon.addch(food[0], food[1], "O")
    else:
        removeTail = snake.pop() #remove the tail
        windon.addch(removeTail[0], removeTail[1], " ")
    windon.addch(snake[0][0], snake[0][1], "O") #present the snake, enjoy :)




