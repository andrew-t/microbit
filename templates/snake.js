// When the BBC micro:bit runs.
function onStart() {
	microbit.say("A&B");
	while (true) {
		globals.x = 2;
		globals.y = 5;
		globals.dx = 0;
		globals.dy = -1;
		globals.length = 2;
		globals.headPointer = 0;
		globals.appleX = 2;
		globals.appleY = 4;
		globals.score = -1;
		globals.movedThisGo = false;
		globals.nextMove = 0;
# LET %MAX = 10
# FOR %N = 0 TO %MAX
		globals.oldX%N = -1;
		globals.oldY%N = -1;
# NEXT %N
		globals.gameOver = false;
		globals.gameStarted = false;
		while (!globals.gameStarted) {
			wait(50);
		}
		while (!globals.gameOver) {
			wait(300);
			globals.x = globals.x + globals.dx;
			globals.y = globals.y + globals.dy;
			if (globals.nextMove == 1) {
				turnLeft();
			}
			if (globals.nextMove == 2) {
				turnRight();
			}
			globals.nextMove = 0;
			globals.movedThisGo = false;
			if ((globals.appleX == globals.x) && (globals.appleY == globals.y)) {
				globals.score = globals.score + 1;
				while (true) {
					globals.appleX = Random.number(0, 4);
					globals.appleY = Random.number(0, 4);
					if (!microbit.isOn(globals.appleX, globals.appleY)) {
						break;
					}
				}
				microbit.on(globals.appleX, globals.appleY);
				if (globals.length < %MAX) {
					globals.length = globals.length + 1;
				}
			} else {
				if (microbit.isOn(globals.x, globals.y)) {
					globals.gameOver = true;
				}
			}
			if ((globals.x < 0) || (globals.y < 0) || (globals.x > 4) || (globals.y > 4)) {
				globals.gameOver = true;
			}
			microbit.on(globals.x, globals.y);
# FOR %N = 0 TO 10
			if (globals.headPointer == %N) {
				globals.oldX%N = globals.x;
				globals.oldY%N = globals.y;
			}
# NEXT %N
			var tailPointer = Math.mod(globals.headPointer + globals.length, %MAX);
# FOR %N = 0 TO 10
			if (tailPointer == %N) {
				microbit.off(globals.oldX%N, globals.oldY%N);
			}
# NEXT %N
			if (globals.headPointer == 0) {
				globals.headPointer = %MAX;
			}
			globals.headPointer = globals.headPointer - 1;
		}
		microbit.say(globals.score);
	}
}

function onPressA() {
	if (globals.movedThisGo) {
		globals.nextMove = 1;
	} else {
		turnLeft();
	}
}

function onPressB() {
	if (globals.movedThisGo) {
		globals.nextMove = 2;
	} else {
		turnRight();
	}
}

function turnLeft() {
	var oldDx = globals.dx;
	globals.dx = globals.dy;
	globals.dy = 0 - oldDx;
	globals.movedThisGo = true;
}

function turnRight() {
	var oldDx = globals.dx;
	globals.dx = 0 - globals.dy;
	globals.dy = oldDx;
	globals.movedThisGo = true;
}

function onPressAandB() {
	globals.gameStarted = true;
}

