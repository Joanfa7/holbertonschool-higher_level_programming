#!/usr/bin/node
const request = require('request');
const process = require('process');

const character = process.argv[2];

request(character, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const nb = JSON.parse(body).results.filter((elem) => {
    return elem.characters.filter((url) => { return url.includes('18'); }).length;
  }).length;
  console.log(nb);
});
