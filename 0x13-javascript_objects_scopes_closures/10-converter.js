#!/usr/bin/node
/*
 * Converts a number from base 10 to another base
 * that is passed as an argument
 */
exports.converter = function (base) {
  return function convert (n) {
    return n.toString(base);
  };
};
