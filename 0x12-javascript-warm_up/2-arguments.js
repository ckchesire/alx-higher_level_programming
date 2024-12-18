#!/usr/bin/node

const { argv } = require('node:process');

// print process.argv
argv.forEach((val, index) => {
  if (index > 2) {
    console.log('Arguments found');
  } else if (index === 2 && !(argv[3])) {
    console.log('Argument found');
  } else if (index === 1 && !(argv[2])) {
    console.log('No argument');
  }
});
