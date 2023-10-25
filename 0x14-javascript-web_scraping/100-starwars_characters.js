#!/usr/bin/node
const request = require('request');

// Construct the SWAPI URL for the film using the command-line argument
const filmId = process.argv[2];
const filmUrl = 'https://swapi-api.hbtn.io/api/films/' + filmId;

// Make an HTTP GET request to fetch information about the film
request(filmUrl, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;

    // Loop through each character in the film
    characters.forEach((characterUrl) => {
      // Make an HTTP GET request for the character's information
      request(characterUrl, function (error, response, body) {
        if (!error) {
          const character = JSON.parse(body).name;
          console.log(character);
        }
      });
    });
  }
});
