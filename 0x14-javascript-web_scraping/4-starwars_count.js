#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    let counter = 0;
    const obj = JSON.parse(body).results;
    for (const key of obj) {
      for (const charac of key.characters) {
        if (charac.search('/18/') > 0) {
          counter++;
        }
      }
    }
    console.log(counter);
  }
});
