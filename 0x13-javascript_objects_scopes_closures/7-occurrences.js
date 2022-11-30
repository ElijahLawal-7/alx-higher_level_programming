#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const reducer = function (count, value) {
    count += (value === searchElement) ? 1 : 0;
    return count;
  };
  return list.reduce(reducer, 0);
};
