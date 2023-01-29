#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const user = {};
    const obj = JSON.parse(body);
    for (const key of obj) {
      if (key.completed === true) {
        if (!(key.userId in user)) {
          user[key.userId] = 1;
        } else {
          user[key.userId]++;
        }
      }
    }
    console.log(user);
  }
});
