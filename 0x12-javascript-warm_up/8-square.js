#!/usr/bin/node

const args1 = process.argv[2];

if (Number(args1)) {
  for (let i = 0; i < args1; i++) {
    console.log('X'.repeat(args1));
  }
} else {
  console.log('Missing size');
}
