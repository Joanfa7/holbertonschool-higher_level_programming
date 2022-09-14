#!/usr/bin/node
const process = require('process');
const request = require('request');

const URL = process.argv[2];


request(URL, (err, response, body) => {
  if (err) {
    console.error(err);
	return;
  }

	const tasks = JSON.parse(body);
	const dic = {};

	for (const task of tasks) {
		if (task.completed) {
			const userID = task.userId;
			dic[userID] = (dic[userID] + 1 || 1);
		}
	}
	console.log(dic);
});
