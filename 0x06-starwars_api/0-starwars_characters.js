#!/usr/bin/node

// Import the request module for making HTTP requests
const request = require('request');

// Get the movie ID from the command-line arguments.
const movieId = process.argv[2];

// Check if the user provided a Movie ID
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

// Construct the URL to fetch film details from the star Wars API
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make the initial request to fetch film data
request(filmUrl, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  if (res.statusCode !== 200) {
    console.error(`Failed to fetch film data: ${res.statusCode}`);
    return;
  }

  // Parse the response body to get the film object.
  const film = JSON.parse(body);

  // Extract 'characters' array conataining URLs to each Character
  const characters = film.characters;

  // Recursively fetch and print each character name in order
  printCharacterNames(characters, 0);
});

/**
 * Recursive function to print character name in order.
 * Ensures each request completes before the next begins,
 * preserving the order from character list.
 *
 * @param {Array} characters - List of character URLs
 * @param {number} index - Current index to process
 */
function printCharacterNames (characters, index) {
  if (index >= characters.length) {
    return; // Base case: All characters printed
  }

  // Fetch the character data from current URL
  request(characters[index], (err, res, body) => {
    if (err) {
      console.error(err);
      return;
    }

    if (res.statusCode !== 200) {
      console.error(`Failed to fetch character ${characters[index]}`);
      return;
    }

    // Parse and print the current character's name
    const character = JSON.parse(body);
    console.log(character.name);

    // Move to the next character
    printCharacterNames(characters, index + 1);
  });
}
