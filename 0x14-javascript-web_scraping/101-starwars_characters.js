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

  // Function to get character name that returns a promise
  function getCharacterName (characterURL) {
    return new Promise((resolve, reject) => {
      request(characterURL, (err, resp) => {
        if (err) {
          reject(err);
        } else {
          const characterInfo = JSON.parse(resp.body);
          resolve(characterInfo.name);
        }
      });
    });
  }

  // Function to print character names in order
  function printCharacterNames (characterURLs) {
    // Create an array of promises from the characterURLs array
    const promises = characterURLs.map(url => getCharacterName(url));

    // Wait for all promises to resolve
    Promise.all(promises)
      .then(names => {
        // Print each name in order
        names.forEach(name => {
          console.log(name);
        });
      })
      .catch(err => {
        console.error('Error fetching character names:', err);
      });
  }

  // Print character names from movieInfo.characters
  printCharacterNames(movieInfo.characters);
});
