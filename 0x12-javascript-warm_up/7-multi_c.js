#!/usr/bin/node
/*
 * Prints `x` times "C is fun"
 */
const firstArg = process.argv[2];
const parsedNumber = parseInt(firstArg);

if (parsedNumber) {
  for (let i = 0; i < parsedNumber; i++) {
    console.log('C is fun');
  }
} else if (process.argv.length < 3) {
  console.log('Missing number of occurrences');
}
