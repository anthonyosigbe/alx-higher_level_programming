#!/usr/bin/node
/* Function to output a Square representation using user-defined characters. */
const BaseSquare = require('./5-square');

module.exports = class Square extends BaseSquare {
  constructor (size) {
    super(size, size);
  }

  double () {
    super.double();
  }

  charPrint (c = 'X') {
    super.print(c);
  }
};
