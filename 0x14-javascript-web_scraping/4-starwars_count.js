#!/usr/bin/node
// Prints the number of movies where "Wedge Antilles" is present

// Import the request module
const request = require('request');

// Retrieve the Star Wars API url
const url = process.argv[2];

// Query the url
request(url, (err, resp) => {
  if (err) console.log(err);
  // Convert the response, a JSON string to JavaScript Object
  const movies = JSON.parse(resp.body);

  let count = 0;
  // For each movie in the array; movies.results
  movies.results.forEach((value) => {
    // For each character in the array; values.characters
    value.characters.forEach((character) => {
      // If the character is Wedge Antilles
      if (character.slice(-3) === '18/') {
        // Increment the count of movies he's in
        count += 1;
      }
    });
  });
  // Print the number of movies Wedge Antilles is in
  console.log(count);
});
