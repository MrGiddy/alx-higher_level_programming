#!/usr/bin/node
// Writes a string to a file

// Import the fs module
const fs = require('node:fs');

// Get file the file path and the string
const file = process.argv[2];
const content = process.argv[3];

// Write content to file
fs.writeFile(file, content, function (err) {
  if (err) {
    console.log(err);
  }
});
