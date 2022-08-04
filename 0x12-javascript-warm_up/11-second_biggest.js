#!/usr/bin/node

if (process.argv.length > 3) {
  const secNum = process.argv.sort(function (a, b) { return b - a; });
  console.log(secNum[3]);
} else {
  console.log(0);
}
