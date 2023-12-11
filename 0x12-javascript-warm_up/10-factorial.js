#!/usr/bin/node
function factorial (n) {
  if (isNaN(n) || n < 0) {
    return 1;
  }

  if (n === 0 || n === 1) {
    return 1;
  }

  return n * factorial(n - 1);
}

const arg = process.argv[2];
const result = factorial(parseInt(arg));

console.log(result);
