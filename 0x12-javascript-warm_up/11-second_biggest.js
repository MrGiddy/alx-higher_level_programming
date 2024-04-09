#!/usr/bin/node
/*
 * Searches the second biggest integer in the list of arguments
 */
if (process.argv.length < 4) {
  console.log(0);
} else {
  const newArgv = process.argv.slice(2);
  for (let i = 0; i < newArgv.length; i++) {
    parseInt(i);
  }
  newArgv.sort().reverse();
  console.log(newArgv[1]);
}
