#!/usr/bin/node
exports.callMeMoby = function (x, callback) {
  for (let i = 0; i < x; i++) {
    callback();
  }
};
