#!/usr/bin/node

const args = process.argv.slice(2);

const firstArg = args[0];
const secondArg = args[1];

if (firstArg !== undefined && secondArg !== undefined) {
  console.log(`${firstArg} is ${secondArg}`);
} else if (firstArg !== undefined && secondArg === undefined) {
  console.log(`${firstArg} is undefined`);
} else if (firstArg === undefined && secondArg === undefined) {
  console.log(`undefined is undefined`);
}
