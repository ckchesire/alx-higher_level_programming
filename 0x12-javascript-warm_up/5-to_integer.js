#!/usr/bin/node

const args = process.argv.slice(2);

const command = args[0];
const number = parseInt(command, 10);

if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${number}`);
}
