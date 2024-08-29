#!/usr/bin/node

const requ = require('request');
const filmId = process.argv[2];
const filmUrl = 'https://swapi-api.alx-tools.com/api/films/' + filmId;

function requestSend (characters, idx) {
  if (characters.length === idx) {
    return;
  }
  requ(characters[idx], (err, res, body) => {
    if (err) {
      console.log(err);
    } else {
      console.log(JSON.parse(body).name);
      requestSend(characters, idx + 1);
    }
  });
}

requ(filmUrl, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const characters = JSON.parse(body).characters;
    requestSend(characters, 0);
  }
});
