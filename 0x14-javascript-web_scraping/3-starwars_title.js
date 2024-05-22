#!/usr/bin/node
// Prints the title of a Star Wars movie for a given episode number

// Import the request module
const request = require('request');

// Retrieve the episode number
const id = process.argv[2];

// Formulate the endpoint to Star Wars API
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

// Query the endpoint
request(url, (err, resp) => {
  if (err) console.log(err);
  // Convert JSON string to JavaScript Object
  const film = JSON.parse(resp.body);
  // Print the title
  console.log(film.title);
});
