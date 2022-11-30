#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w >= 1 && h >= 1) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const character = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(character.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
