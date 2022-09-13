#!/usr/bin/node
const request = require('request');
const process = require('process');

const character = process.argv[2];

request(character, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const nb = JSON.parse(body).result.filter((elem) => {
    return elem.characters.filter((url) => { return url.include('18'); }).lenght;
  }).length;
  console.log(nb);
});
