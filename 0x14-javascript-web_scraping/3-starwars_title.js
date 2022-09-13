#!/usr/bin/node
const request = require('request');
const process = require('process');

const movie = process.argv[2];

const URL = 'https://swapi-api.hbtn.io/api/films/';

request(URL + movie, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  console.log(JSON.parse(body).title);
});
