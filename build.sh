#!/usr/bin/env sh

for f in *.py
do
	if [ "$f" != "global.py" ]
	then
		echo "Processing $f file..."
		./py2hex.js $f
		echo "Done."
	fi
done