#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const argv = process.argv;
const url = argv[2];
const file = argv[3];
request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    fs.writeFile(file, body, 'utf8', function (err) {
      if (err) return console.log(err);
    });
  }
});
