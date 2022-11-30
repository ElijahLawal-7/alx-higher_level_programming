#!/usr/bin/node
exports.logMe = function (item) {
  if (!this.count) {
    this.count = 0;
  }
  console.log(`${this.count}: ${item}`);
  this.count++;
};
