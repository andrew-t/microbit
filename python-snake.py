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
    return image.get_pixel(pos['x'], pos['y'])

def light_pixel(image, pos, value = 9):
    image.set_pixel(pos['x'], pos['y'], value)

def unlight_pixel(image, pos):
    light_pixel(image, pos, 0)

a_pressed = False
b_pressed = False
on_double = False
done_this_double = False
def button_sleep(time, doubles = True, queue = []):
    global a_pressed
    global b_pressed
    global on_double
    global done_this_double
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
                done_this_double = False
            if on_double and not done_this_double and (not button_a.is_pressed() or not button_b.is_pressed()):
                queue.append('ab')
                done_this_double = True
        else:
            on_double = False
            done_this_double = False
        if not on_double:
            if not button_a.is_pressed() and a_pressed:
                queue.append('a')
            elif not button_b.is_pressed() and b_pressed:
                queue.append('b')
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
