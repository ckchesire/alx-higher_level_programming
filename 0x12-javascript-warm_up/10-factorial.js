#!/usr/bin/node

const args = process.argv.slice(2);
const firstNum = parseInt(args[0], 10);

function factorial (a) {
  if (a === 1) {
    return (1);
  }
  else {
    return a * factorial(a - 1);
  }
}
if (isNaN(firstNum)) {
  console.log('1');
} else {
  console.log(`${factorial(firstNum)}`);
}
