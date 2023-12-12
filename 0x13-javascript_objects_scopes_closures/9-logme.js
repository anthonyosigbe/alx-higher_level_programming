#!/usr/bin/node
/* function that prints the number of arguments already printed
 * and the new argument value */
let iteration = 0;

exports.logMe = function count (item) {
  console.log(`${iteration}: ${item}`);
  iteration += 1;
};
