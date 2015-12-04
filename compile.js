#!/usr/bin/env node

var fs = require('fs');
fs.readdir('templates', function (err, data) {
	if (err)
		return console.err(err);
	data.forEach(function (fn) {
		if (/\.js$/.test(fn)) fs.readFile('templates/' + fn, function (err, text) {
			if (err)
				return console.err(err);
			var out = [],
				input = text.toString().split('\n'),
				vars = {},
				fors = {},
				loops = [];
			for (var i = 0; i < input.length; ++i) {
				var line = input[i];
				for (var sub in vars)
					line = line.replace(new RegExp(sub, 'g'), vars[sub]);
				if (!/^#/.test(line)) {
					out.push(line);
				} else {
					var parts = line.split(' ').filter(function (part) {
						return part;
					});
					switch (parts[1]) {
						case 'FOR':
							fors[parts[2]] = {
								to: parseInt(parts[6], 10),
								line: i,
								step: parts[8] ? parseInt(parts[8], 10) : 1
							};
							loops.push(parts[2]);
						case 'LET':
							vars[parts[2]] = parseInt(parts[4], 10);
							break;
						case 'NEXT':
							var loop = loops.pop();
							vars[loop] += fors[loop].step;
							if (vars[loop] != fors[loop].to) {
								loops.push(loop);
								i = fors[loop].line;
							} else {
								delete vars[loop];
								delete fors[loop];
							}
							break;
					}
				}
			}
			fs.writeFile('output/' + fn, out.join('\n'));
		});
	})
});