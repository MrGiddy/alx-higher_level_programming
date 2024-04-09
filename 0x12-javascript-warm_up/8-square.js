#!/usr/bin/node
/*
 * Prints a square
 */
const firstArg = process.argv[2];
const parsedNumber = parseInt(firstArg);

if (process.argv.length < 3) {
  console.log('Missing size');
} else if (parsedNumber) {
  for (let i = 0; i < parsedNumber; i++) {
    let row = '';
    for (let j = 0; j < parsedNumber; j++) {
      row += '#';
    }
    console.log(row);
  }
}
