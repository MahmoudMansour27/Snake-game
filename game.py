import random
import  curses

screen = curses.initscr()
curses.curs_set(0)
screen_hight, screen_width = screen.getmaxyx()
windon = curses.newwin(screen_hight,screen_width, 0,0)
windon.keypad(1)
windon.timeout(100)
snk_x = screen_width//4
snk_y = screen_hight//2
snake =[
    [snk_y, snk_x],
    [snk_y-1, snk_x],
    [snk_y-2, snk_x]
]
food = [screen_hight//2, screen_width//2]
windon.addch(food[0], food[1], curses.ACS_BTEE)
key = curses.KEY_RIGHT
while True:
    nextKey = windon.getch()
    key = key if nextKey == -1 else nextKey
    if snake[0][0] in [0, screen_width] or  snake[0][0] in [0, screen_hight] or snake[0][0] in [screen_hight, screen_width] or snake[0] in snake[1:]:
        curses.endwin()
        quit()
    newPosition = [snake[0][0], snake[0][1]]
    if key == curses.KEY_RIGHT:
        newPosition[1] += 1
    elif key == curses.KEY_LEFT:
        newPosition[1] += -1
    elif key == curses.KEY_UP:
        newPosition[0] += 1
    elif key == curses.KEY_DOWN:
        newPosition[0] += -1

    snake.insert(0, newPosition)
    if snake[0] == food:
        food = None
        while (food == None):
            newFood = [random.randint(1, screen_hight-1), random.randint(1, screen_width-1)]
            food = newFood if newFood not in snake else None
        windon.addch(food[0], food[1], curses.ACS_BTEE)
    else:
        removeTail = snake.pop()
        windon.addch(removeTail[0], removeTail[1], '')
    windon.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)




