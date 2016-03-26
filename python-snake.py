from microbit import *
import random

snake = Image("55550:50050:50000:50090:55000")
score = 0

def play_game():
    global score
    while button_a.is_pressed() or button_b.is_pressed():
        pass
    score = 0
    play_snake()
    display.scroll(str(score))
    while not button_a.is_pressed() or not button_b.is_pressed():
        pass
    while button_a.is_pressed() or button_b.is_pressed():
        pass

def choose_game():
    display.show(snake)
    while True:
        if button_a.is_pressed() and button_b.is_pressed():
            play_game()
            display.show(snake)

def is_lit(image, pos):
    if pos['x'] < 0 or pos['x'] >= 5 or pos['y'] < 0 or pos['y'] >= 5:
        return False
    return image.get_pixel(pos['x'], pos['y'])

def light_pixel(image, pos, value = 9):
    if pos['x'] >= 0 and pos['x'] < 5 and pos['y'] >= 0 and pos['y'] < 5:
        image.set_pixel(pos['x'], pos['y'], value)

def unlight_pixel(image, pos):
    light_pixel(image, pos, 0)

a_was_pressed = False
b_was_pressed = False
on_double = False
done_this_double = False
def button_sleep(time, doubles = True, queue = None):
    global a_was_pressed
    global b_was_pressed
    global on_double
    global done_this_double
    if queue == None:
        queue = []
    while time > 0:
        sleep(10)
        time -= 10
        a_down = button_a.is_pressed()
        b_down = button_b.is_pressed()
        a_released = a_was_pressed and not a_down
        b_released = b_was_pressed and not b_down
        a_pressed = not a_was_pressed and a_down
        b_pressed = not b_was_pressed and b_down
        if doubles:
            # if a second button goes down it is a new double.
            if a_down and b_down and (a_pressed or b_pressed):
                on_double = True
            # if one of two buttons is released, that's a double-press
            if a_was_pressed and b_was_pressed and (a_released or b_released):
                queue.append('ab')
            # if the last button is released, clear the double.
            if not a_was_pressed and not b_was_pressed:
                on_double = False
        else:
            on_double = False
        if not on_double:
            if a_released:
                queue.append('a')
            if b_released:
                queue.append('b')
        a_was_pressed = a_down
        b_was_pressed = b_down
    return queue

def random_pos():
    return { 'x': random.randint(0, 4), 'y': random.randint(0, 4) }

def play_snake():
    global score
    pip = None
    pip = random_pos()
    im = Image(5, 5)
    length = 3
    maxLength = 20
    positions = [ { 'x': 2, 'y': 5 } ] * maxLength
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
