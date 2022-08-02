#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
	constructor (size) {
		super(size, size);
	}
	charPrint (c){
		if (typeof c === 'undefined'){
			this.print();
		} else {
			let i, j;
			for (i = 0; i < this.height; i++){
				for (j = 0; j < this.width; j++) { process.stdout.write('X'); }
				console.log('');

			}
		}
	}
}
module.exports = Square;
