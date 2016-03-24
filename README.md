# micro:bit games

Here are some games I've written for the [BBC micro:bit](https://www.microbit.co.uk/). In most of the games it will display your score on game over. You can play again with either the reset button on the back or (for the simpler games) by pressing A and B together on the game over screen.

To run them, click the 'hex' link, then right click the 'raw' button and save the linked file. Drag that onto your micro:bit and it should flash.

## micro:tetris [js](templates/tetris.js) | [hex](output/tetris.hex)
Press A or B to move a block left or right. Press both buttons at once to rotate a block. The blocks are smaller than in real Tetris (and you can't do that stupid cheat where you endlessly rotate a block so it never settles that licensed Tetris games are obliged to put in.)

## micro:snake [js](templates/snake.js) | [hex](output/snake.hex)
Press A or B to turn left or right.

## micro:maze [js](templates/tetris.js) | [hex](output/tetris.hex)
A very crude first-person 3D maze game. Press A or B to turn 90º, or press A and B together to walk forward one square.

## 2:cars [js](templates/2cars.js) | [hex](output/2cars.hex)
The "two cars" phone app: on each side of the screen is a car driving past a series of obstacles. Press A to switch lanes for the left hand car, or B to switch lanes for the right hand car.

# Writing code

To get around a few limitations of the micro:bit code editor, I have written [a very basic preprocessor](compile.js) which allows me to polyfill a few more vital features the native implementation does not support. Therefore, the full process to modidy a game is:

1. Clone this repo and install Nodejs
2. Edit the file in [`templates`](templates).
3. Run [`compile.js`](compile.js).
4. Paste the result into the code editor at [microbit.co.uk/app](https://www.microbit.co.uk/app)
5. Download the hex file
6. Flash the hex file to the micro:bit

Or you can run it in the in-browser emulator.

Because this is all a bit of a pain, I have [included the output files in the repo](output).

# micro:bit code generator

## micro:bit "Javascript" limitations

* You can't call a function.
* You must always use braces around `if` statements etc — in particular you cannot use `else if`. You must use `else { if ... }`
* You can't use `switch`.
* Variables are treated as strongly typed.
* You can't use arrays or objects.
* You can't use increment operators, even in for loops. Use `i = i + 1`.
* You can't declare variables outside a function; put them on `globals`.
* You can't declare variables without also assigning them.
* You can't declare two variables on one line (`var a = 1, b = 2;`).
* You can't use non-integer numbers. `3/2 == 1`.

## Generator limitations:

You can call functions now, but they *must* be written exactly as so:

```
function functionName() {
	// code goes here
}
```

You cannot pass arguments to a function. You cannot make functions recursive, even in unreachable code paths, as they are inlined.

You cannot place two statements on a line if they need re-writing (eg, function calls).

## Future ideas

Using a real lexer/parser, we could:

* polyfill function arguments;
* remove syntax limitations.
