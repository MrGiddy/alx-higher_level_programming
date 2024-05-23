#!/usr/bin/node
// Gets the contents of a webpage and stores it in a file

// Import request and fs modules
const request = require('request');
const fs = require('node:fs');

// Get the URL to request
const url = process.argv[2];
// Get the file path to store the webpage
const file = process.argv[3];

// Get the content of the webpage
request(url, (err, resp, body) => {
  if (err) console.log(err);
  // Store the content in file
  fs.writeFile(file, body, 'utf8', (err) => {
    if (err) console.log(err);
  });
});
