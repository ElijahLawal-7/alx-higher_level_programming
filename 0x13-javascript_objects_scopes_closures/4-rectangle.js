#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let s = this.height;
    while (s) {
      console.log('X'.repeat(this.width));
      s--;
    }
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }

  rotate () {
    const change = this.width;
    this.width = this.height;
    this.height = change;
  }
};
