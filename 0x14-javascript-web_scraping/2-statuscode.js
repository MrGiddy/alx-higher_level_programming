#!/usr/bin/node
// Displays the status code of a GET request

// Import the request module
const request = require('request');

// Get the url to query
const url = process.argv[2];

// Query the url
request(url, (err, resp) => {
  // Display the error if it occurred
  if (err) console.log(err);
  // Display the status code of the response
  console.log(resp.statusCode);
});
