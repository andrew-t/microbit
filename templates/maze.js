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


}

function isWall() {
	if ((globals.inMazeX == 0) || (globals.inMazeX == 14))
		globals.isWall = true;
	else if (globals.inMazeY == 0) {
		globals.isWall = (globals.inMazeX != 6);
	} else if (globals.inMazeY == 1) {
		globals.isWall = (globals.inMazeX == 9);
	} else if (globals.inMazeY == 2) {
		globals.isWall = (globals.inMazeX != 3) && (globals.inMazeX != 10) && (globals.inMazeX != 13);
	} else if (globals.inMazeY == 3) {
		globals.isWall = (globals.inMazeX == 8);
	} else if (globals.inMazeY == 4) {
		globals.isWall = (globals.inMazeX != 15) && (globals.inMazeX != 11);
	} else if (globals.inMazeY == 5) {
		globals.isWall = false;
	} else if (globals.inMazeY == 6) {
		globals.isWall = (globals.inMazeX != 3) && (globals.inMazeX != 10) && (globals.inMazeX != 13);
	} else if (globals.inMazeY == 7) {
		globals.isWall = (globals.inMazeX == 7);
	} else if (globals.inMazeY == 8) {
		globals.isWall = (globals.inMazeX != 4) && (globals.inMazeX != 19);
	} else if (globals.inMazeY == 9) {
		globals.isWall = false;
	} else if (globals.inMazeX == 10) {
		globals.isWall = true;
	}
}