#!/usr/bin/node
const argv = process.argv;
const x = parseInt(argv[2]);
const character = 'X';
if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    console.log(character.repeat(x));
  }
}
