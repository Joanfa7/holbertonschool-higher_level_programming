#!/usr/bin/node
const process = require('process');
const fs = require('fs');

const file = process.argv[2];
const script = process.argv[3];

fs.writeFile(
  file,
  script,
  function (err) {
    if (err) {
      return console.error(err);
    }
  });
