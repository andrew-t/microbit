/*
	012345678901234
0	@@@@@@ @@@@@@@@
1	@        @    @
2	@@@ @@@@@@ @@ @
3	@       @     @
4	@@@@@ @@@@@ @@@
5	@             @
6	@@@ @@@@@@@@@ @
7	@     *@      @
8	@@@@ @@@@ @@@@@
9	@             @
10	@@@@@@@@@@@@@@@
	012345678901234

*/

function onStart() {
	//_.say('A&B');
	$.inMazeX = 0;
	$.inMazeY = 0;
	$.isWall = false;
	$.x = 6;
	$.y = 7;
	$.dx = -1;
	$.dy = 1;
	drawMaze();
}

function onPressA() {
	var dx = $.dx;
	$.dx = $.dy;
	$.dy = 0 - dx;
	drawMaze();
}

function onPressB() {
	var dx = $.dx;
	$.dx = 0 - $.dy;
	$.dy = dx;
	drawMaze();
}

function onPressAandB() {
	$.inMazeX = $.x + $.dx;
	$.inMazeY = $.y + $.dy;
	isWall();
	if (!$.isWall) {
		$.x = $.inMazeX;
		$.y = $.inMazeY;
		drawMaze();
	}
}

/*
	BCD
	A*E
*/

function drawMaze() {
	$.inMazeX = $.x + $.dy;
	$.inMazeY = $.y - $.dx;
	isWall();
	var a = $.isWall;
	$.inMazeX = $.x + $.dy + $.dx;
	$.inMazeY = $.y - $.dx + $.dy;
	isWall();
	var b = $.isWall;
	$.inMazeX = $.x + $.dx;
	$.inMazeY = $.y + $.dy;
	isWall();
	var c = $.isWall;
	$.inMazeX = $.x - $.dy + $.dx;
	$.inMazeY = $.y + $.dx + $.dy;
	isWall();
	var d = $.isWall;
	$.inMazeX = $.x - $.dy;
	$.inMazeY = $.y + $.dx;
	isWall();
	var e = $.isWall;
	_.clear();
	if (a) { _.on(0, 0); _.on(0, 4); }
	if (b && !a) { _.on(0, 1); _.on(0, 3); }
	if (!a && !b) { _.on(0, 2); }
	if (c || (a && !b) || !a) { _.on(1, 1); _.on(1, 3); }
	if (c) { _.on(2, 1); _.on(2, 3); } else { _.on(2, 2); }
	if (c || (e && !d) || !e) { _.on(3, 1); _.on(3, 3); }
	if (!e && !d) { _.on(4, 2); }
	if (d && !e) { _.on(4, 1); _.on(4, 3); }
	if (e) { _.on(4, 0); _.on(4, 4); }
}

function isWall() {
	if ($.inMazeY < 0) {
		$.isWall = false;
	} else { if (($.inMazeX == 0) || ($.inMazeX == 14)) {
		$.isWall = true;
	} else { if ($.inMazeY == 0) {
		$.isWall = ($.inMazeX != 6);
	} else { if ($.inMazeY == 1) {
		$.isWall = ($.inMazeX == 9);
	} else { if ($.inMazeY == 2) {
		$.isWall = ($.inMazeX != 3) && ($.inMazeX != 10) && ($.inMazeX != 13);
	} else { if ($.inMazeY == 3) {
		$.isWall = ($.inMazeX == 8);
	} else { if ($.inMazeY == 4) {
		$.isWall = ($.inMazeX != 15) && ($.inMazeX != 11);
	} else { if ($.inMazeY == 5) {
		$.isWall = false;
	} else { if ($.inMazeY == 6) {
		$.isWall = ($.inMazeX != 3) && ($.inMazeX != 10) && ($.inMazeX != 13);
	} else { if ($.inMazeY == 7) {
		$.isWall = ($.inMazeX == 7);
	} else { if ($.inMazeY == 8) {
		$.isWall = ($.inMazeX != 4) && ($.inMazeX != 19);
	} else { if ($.inMazeY == 9) {
		$.isWall = false;
	} else { if ($.inMazeX == 10) {
		$.isWall = true;
	} else {
		$.isWall = false;
	}}}}}}}}}}}}}
}