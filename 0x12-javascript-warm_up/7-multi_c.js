#!/usr/bin/node

const args = process.argv.slice(2);
const comment = 'C is fun';
const times = parseInt(args[0], 10);

if (isNaN(times)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < times; i++) {
    console.log(`${comment}`);
  }
}
