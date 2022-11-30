#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};

for (const key in dict) {
  if (typeof (newDict[dict[key]]) === 'undefined') {
    newDict[dict[key]] = [];
  }
  newDict[dict[key]].push(key);
}

console.log(newDict);
