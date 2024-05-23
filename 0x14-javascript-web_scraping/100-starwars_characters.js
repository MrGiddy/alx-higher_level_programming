#!/usr/bin/node
// Prints all characters of a Star Wars movie

// Import the request module
const request = require('request');

// Get the Movie ID - example: 3 = "Return of the Jedi"
const movieId = process.argv[2];

// Endpoint to hit: The Star Wars API URL + movie_id
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Query the url
request(url, (err, resp) => {
  if (err) console.log(err);
  // Convert the response, a JSON string to JavaScript Object
  const movieInfo = JSON.parse(resp.body);
  // Retrieve the list of actor urls
  const charactersUrls = movieInfo.characters;

  // Get info for each character and retrieve their name
  charactersUrls.forEach((characterURL) => {
    request(characterURL, (err, resp) => {
      if (err) console.log(err);
      const characterInfo = JSON.parse(resp.body);
      // Display the character's name
      console.log(characterInfo.name);
    });
  });
});
