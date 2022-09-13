#!/usr/bin/node
const process = require('process');
const axios = require('axios').default;

const URL = process.argv[2];

axios.get(URL)
  .then(function (response) {
    for (const key in response) {
      if (key === 'status') {
        console.log(`code: ${response[key]}`);
      }
    }
  })
  .catch(function (error) {
    // handle error
    console.log(error.response.status);
  });
