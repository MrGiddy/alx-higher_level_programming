#!/usr/bin/node
/*
 * Prints: My number: <first arg. converted to int.>
 * if the first argument is convertable to integer
 */
const firstArg = process.argv[2];
// Regex matching integers or floats
const validNumberRegex = /^(\+|-)?\d+(\.\d+)?$/;

if (validNumberRegex.test(firstArg)) {
  console.log('My number:', parseInt(firstArg));
} else {
  console.log('Not a number');
}
