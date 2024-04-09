#!/usr/bin/node
/*
 * Computes and prints a factorial
 * Factorial of NaN is 1
 */
const n = parseInt(process.argv[2]);

function factorial (n) {
  if (!n) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

console.log(factorial(n));
