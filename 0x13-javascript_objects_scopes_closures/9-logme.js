#!/usr/bin/node

let str = 0;

exports.logMe = function (item) {
  console.log(str + ': ' + item);
  str++;
};
