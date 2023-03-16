#!/usr/bin/node
// logme

let numberPrinted = 0;

exports.logMe = function (item) {
  console.log(`${numberPrinted}: ${item}`);
  numberPrinted++;
};
