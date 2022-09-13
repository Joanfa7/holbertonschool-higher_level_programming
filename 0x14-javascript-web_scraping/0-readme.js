#!/usr/bin/node
const process = require('process');
const fs = require('fs');

const file = process.argv[2];

fs.readFile(file, 'utf8', function (err, data) {
  if (err) {
    return console.error(err);
  }
  console.log(data.toString());
});
