#!/usr/bin/node
/*
 * Imports a dictionary of occurrences by user id
 * Computes a dictionary of user ids by occurrence
 *
 */
const { dict } = require('./101-data');
const newDict = {}; // will contain ids by occurrences

for (const [key, value] of Object.entries(dict)) {
  if (!(value in newDict)) {
    newDict[value] = [];
  }
  newDict[value].push(key);
}

console.log(newDict);
