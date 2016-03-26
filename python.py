from microbit import *
import random

tetris = Image("00090:00990:90000:99909:90999")
snake =  Image("55550:50050:50000:50090:55000")
games = [ tetris, snake ]
game = 0
score = 0

def play_game():
    global tetris
    global snake
    global games
    global game
    global score
    while button_a.is_pressed() or button_b.is_pressed():
        pass
    score = 0
    if games[game] == tetris:
        play_tetris()
    elif games[game] == snake:
        play_snake()
    else:
        return
    display.scroll(str(score))
    while not button_a.is_pressed() or not button_b.is_pressed():
        pass
    while button_a.is_pressed() or button_b.is_pressed():
        pass

def choose_game():
    global games
    global game
    while True:
        display.show(games[game])
        if button_a.is_pressed():
            played = False
            while button_a.is_pressed():
                if button_b.is_pressed():
                    play_game()
                    played = True
            if not played:
                game = (game + 1) % len(games)
        elif button_b.is_pressed():
            played = False
            while button_b.is_pressed():
                if button_a.is_pressed():
                    play_game()
                    played = True
            if not played:
                game = (game - 1) % len(games)

def is_lit(image, pos):
    return image.get_pixel(pos['x'], pos['y'])

def light_pixel(image, pos, value = 9):
    image.set_pixel(pos['x'], pos['y'], value)

def unlight_pixel(image, pos):
    light_pixel(image, pos, 0)

a_pressed = False
b_pressed = False
on_double = False
def button_sleep(time, doubles = True, queue = []):
    global a_pressed
    global b_pressed
    global on_double
    while time > 0:
        a_pressed = button_a.is_pressed()
        b_pressed = button_b.is_pressed()
        sleep(10)
        time -= 10
        if doubles:
            if a_pressed and b_pressed:
                on_double = True
            elif not a_pressed and not b_pressed:
                on_double = False
            if on_double and (not button_a.is_pressed() or not button_b.is_pressed()):
                queue.append('ab')
        if not on_double:
            if not button_a.is_pressed() and a_pressed:
                queue.append('a')
            elif not button_b.is_pressed() and b_pressed:
                queue.append('b')
    return queue

def random_pos():
    return { 'x': random.randint(0, 4), 'y': random.randint(0, 4) }

def play_tetris():
    global score
    im = Image(5, 5)
    block = None
    while True:
        block = random.randint(0, 7)
        if block == 0:
            block = [ [ [ 9 ] ] ]
        elif block <= 2:
            block = [ [ [ 7, 7 ] ], [ [ 7 ], [ 7 ] ] ]
        elif block <= 6:
            block = [ [ [ 5, 5 ], [ 5, 0 ] ], [ [ 5, 5 ], [ 0, 5 ] ], [ [ 0, 5 ], [ 5, 5 ] ], [ [ 5, 0 ], [ 5, 5 ] ] ]
        else:
            block = [ [ [ 3, 3 ], [ 3, 3 ] ] ]
        orientation = random.randint(0, len(block))
        x = 2
        y = -1
        while True:
            for n in range(0, 30):
                display.show(im)
                for press in button_sleep(10, True):
                    if press == 'a':
                        orientation = (orientation - 1) % len(block)
                    elif press == 'b':
                        orientation = (orientation + 1) % len(block)


def play_snake():
    global score
    pip = None
    pip = random_pos()
    im = Image(5, 5)
    length = 3
    maxLength = 20
    positions = [ { 'x': 2, 'y': 4 } ] * maxLength
    headPointer = 2
    tailPointer = 0
    dx = 0
    dy = -1
    queue = []
    while True:
        nextPointer = (headPointer + 1) % maxLength
        # turn if need be
        if len(queue) > 0:
            button = queue[0]
            queue = queue[1:]
            if button == 'a':
                temp = dx
                dx = dy
                dy = -temp
            elif button == 'b':
                temp = dx
                dx = -dy
                dy = temp
        # advance one place
        positions[nextPointer] = { 'x': positions[headPointer]['x'] + dx, 'y': positions[headPointer]['y'] + dy }
        headPointer = nextPointer
        head = positions[headPointer]
        # die, eat a pip or advance the tail
        if head['x'] < 0 or head['x'] > 4 or head['y'] < 0 or head['y'] > 4 or is_lit(im, head) == 5:
            break
        elif head['x'] == pip['x'] and head['y'] == pip['y']:
            score = score + 1
            while is_lit(im, pip) > 0:
                pip = random_pos()
        else:
            unlight_pixel(im, positions[tailPointer])
            tailPointer = (tailPointer + 1) % maxLength
        # update the screen
        light_pixel(im, head, 5)
        light_pixel(im, pip)
        display.show(im)
        button_sleep(400, False, queue)

choose_game()
