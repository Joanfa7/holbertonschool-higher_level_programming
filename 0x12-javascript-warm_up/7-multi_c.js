#!/usr/bin/node

const args1 = process.argv[2];

if (Number(args1)) {
  for (let i = 0; i < args1; i++) { console.log('C is fun'); }
} else {
  console.log('Missing number of occurrences');
}
