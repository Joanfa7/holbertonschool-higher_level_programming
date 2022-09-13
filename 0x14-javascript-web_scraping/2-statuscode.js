#!/usr/bin/node
const process = require('process');
const fs = require('fs');
const axios = require('axios').default;

const URL = process.argv[2];

axios.get(URL)
  .then(function (response) {
	for(var key in response){
		if( key == "status"){
		console.log(`code: ${response[key]}`);
		}
	}
  })



