#!/usr/bin/node
/*
 * Prints the first argument passed to it
 */
const numArgs = process.argv.length;

if (numArgs < 3) {
  console.log('No Argument');
} else {
  console.log(process.argv[2]);
}
