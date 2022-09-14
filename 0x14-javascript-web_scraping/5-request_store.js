#!/usr/bin/node
const process = require('process');
const fs = require('fs');
const request = require('request');

const URL = process.argv[2];
const file = process.argv[3];

request(URL, function (err, response, body) {
  if (err) {
    console.error('error:', err);
  }
  fs.writeFile(file, body, 'utf-8', (err) => {
    if (err) {
      console.error('error:', err);
    }
  });
});
