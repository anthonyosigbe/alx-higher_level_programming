#!/usr/bin/node
/* Defines a Square class that inherits from the Rectangle class. */
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  double () {
    super.double();
  }
};
