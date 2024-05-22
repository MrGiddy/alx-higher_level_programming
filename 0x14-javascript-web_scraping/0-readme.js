#!/usr/bin/node

// Import the fs module
const fs = require('node:fs');

// Get the filename from command line
const file = process.argv[2];

// Read and display the contents of the file
fs.readFile(file, 'utf8', function (err, contents) {
  if (err) {
    console.log(err);
    return;
  }
  console.log(contents);
});
