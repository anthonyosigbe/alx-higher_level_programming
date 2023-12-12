#!/usr/bin/node

/* Transforms a decimal number into a different base
 * specified as an argument using a closure. */

exports.converter = function (base) {
  function myConverter (n) {
    return n.toString(base);
  }

  return myConverter;
};
