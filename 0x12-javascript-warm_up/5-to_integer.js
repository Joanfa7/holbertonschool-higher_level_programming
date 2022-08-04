#!/usr/bin/node

const { argv } = require('process');
const args1 = parseInt(argv[2]);

if (Number(args1)){
	console.log('My number: ', + Number(args1));
}else{
	console.log('Not a number');
}
