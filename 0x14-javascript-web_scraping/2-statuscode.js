#!/usr/bin/node
const process = require('process');
const fs = require('fs');
const axios = require('axios').default;

const URL = process.argv[2];

axios.get(URL)
  .then(function (response) {
    // handle success
    console.log(response);
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  })
 /* .then(function () {
    // always executed
  });*/


