#!/usr/bin/node
exports.converter = function (base) {
  return function (input) {
    return input.toString(base);
  };
};
