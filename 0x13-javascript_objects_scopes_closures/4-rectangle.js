#!/usr/bin/node
/*  Increase the dimensions of the Rectangle by doubling both width and height,
 *  and perform a rotation */
module.exports = class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && typeof h === 'number' && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (char = 'X') {
    for (let i = 0; i < this.height; ++i) {
      console.log(char.repeat(this.width));
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
