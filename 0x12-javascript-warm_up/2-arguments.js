#!/usr/bin/node
/*
 * Prints a message depending on the number of arguments passed
 */
const numArgs = process.argv.length;

if (numArgs < 3) {
  console.log('No argument');
} else if (numArgs === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
