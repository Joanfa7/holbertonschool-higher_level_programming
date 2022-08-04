#!/usr/bin/node

const args1 = process.argv[2];

if (Number(args1)) {
  console.log('My number: ', args1);
} else {
  console.log('No a number');
}
