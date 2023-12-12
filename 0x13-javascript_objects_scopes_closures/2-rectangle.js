#!/usr/bin/node
/* Validate Rectangle parameters */

module.exports = class Rectangle {
  constructor (w, h) {
    /* Ensure width and height are numbers and positive */
    if (typeof w === 'number' && typeof h === 'number' && w > 0 && h > 0) {
      /* Assign valid width and height to the object */
      this.width = w;
      this.height = h;
    }
  }
};
