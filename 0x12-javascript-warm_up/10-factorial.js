#!/usr/bin/node
function factorial (n) {
  if (isNaN(n) || n < 2) return 1;
  else return n * factorial(n - 1);
}
console.log(factorial(process.argv[2]));
