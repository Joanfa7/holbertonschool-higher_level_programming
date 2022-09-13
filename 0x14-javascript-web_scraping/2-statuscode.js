#!/usr/bin/node
const process = require('process');
const axios = require('axios').default;



const URL = process.argv[2];

axios.get(URL)
	.then(function (response) {
		console.log(`code ${response.status}`);
	})
	.catch(function (error) {
		// handle error
		console.log(`code: ${error.response.status}`);
	});
